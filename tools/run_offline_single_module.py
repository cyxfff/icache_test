import argparse
import json
import os
import re
import shutil
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import METRIC_KEYS, build_base_cfg, build_knobs
from experiments.csv_layout import join_case_labels, metric_headers, with_metric_separators
from experiments.experiment_config import MODULE_LIBRARY_SUITE
from experiments.runner import build_single_cfg
from tools.run_single_module import parse_csv_list, build_filtered_suite
from utils import build_offline_binary, parse_run_log_file, write_csv_row
CSV_PREFIX = ["suite", "case", "order_tag", "modules"]


def safe_name(text, max_len=140):
    text = re.sub(r"[^A-Za-z0-9_.+-]+", "_", str(text))
    text = text.strip("_")
    if not text:
        text = "case"
    return text[:max_len]


def make_case_id(index, case):
    """
    case_id 必须唯一。

    注意：
    - 不只用 module 名，因为同一个 module 下可能有多个参数 case。
    - 前面加 index，保证不会覆盖。
    """
    label = case.get("label") or case.get("module") or "case"
    return f"{index:04d}_{safe_name(label)}"


def build_headers(metric_keys):
    return [*CSV_PREFIX, *metric_headers(metric_keys)]


def tag_row(row, suite_name, case_name, order_tag, modules_tag):
    tagged = dict(row)
    tagged["suite"] = suite_name
    tagged["case"] = case_name
    tagged["order_tag"] = order_tag
    tagged["modules"] = modules_tag
    return tagged


def to_jsonable(value):
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_jsonable(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(to_jsonable(obj), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def write_manifest_tsv(records, path):
    """
    给远程 run.sh 用的最小清单。

    格式：
        case_id<TAB>bin<TAB>log

    run.sh 只需要读取这三个字段：
        bin 是相对远程 WORKDIR 的路径
        log 是相对远程 WORKDIR 的路径
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as handle:
        handle.write("case_id\tbin\tlog\n")
        for record in records:
            handle.write(
                f"{record['case_id']}\t"
                f"{record['bin']}\t"
                f"{record['log']}\n"
            )


def copy_runner_script(runner_sh, offline_dir):
    """
    把同目录下的 run.sh 复制到离线输出目录。
    如果你远程有固定 run.sh，也可以不用这个文件。
    """
    runner_sh = Path(runner_sh)
    if not runner_sh.is_absolute():
        runner_sh = SCRIPT_DIR / runner_sh

    if not runner_sh.exists():
        raise FileNotFoundError(f"runner script not found: {runner_sh}")

    dst = Path(offline_dir) / "run.sh"
    shutil.copy2(runner_sh, dst)
    dst.chmod(dst.stat().st_mode | 0o111)
    return dst


def apply_knob_overrides(knobs, args):
    """
    prepare 阶段允许临时覆盖交叉编译相关配置。
    不涉及远程运行。
    """
    if args.cc:
        knobs["cc"] = args.cc

    if args.target:
        knobs["target"] = args.target

    if args.sysroot:
        knobs["sysroot"] = args.sysroot

    extra_cflags = parse_csv_list(args.extra_cflags)
    if extra_cflags:
        knobs["extra_cflags"] = list(knobs.get("extra_cflags") or []) + extra_cflags

    extra_ldflags = parse_csv_list(args.extra_ldflags)
    if extra_ldflags:
        knobs["extra_ldflags"] = list(knobs.get("extra_ldflags") or []) + extra_ldflags

    return knobs


def build_suite_cfg(args):
    """
    完全复用原 run_single.py 的过滤逻辑。
    --modules / --case-contains / --max-cases 都只是过滤 case 集合。
    """
    suite_cfg = build_filtered_suite(
        MODULE_LIBRARY_SUITE,
        parse_csv_list(args.modules),
        args.case_contains,
        args.max_cases,
    )

    if args.iters is not None or args.rounds is not None:
        run_defaults = dict(suite_cfg.get("run_defaults", {}))
        if args.iters is not None:
            run_defaults["iters"] = max(1, int(args.iters))
        if args.rounds is not None:
            run_defaults["rounds"] = max(1, int(args.rounds))
        suite_cfg["run_defaults"] = run_defaults

    if not suite_cfg["cases"]:
        raise ValueError("no single-module cases matched filters")

    return suite_cfg


def default_offline_dir(root):
    return (root / "offline_run_single_module").resolve()


def prepare_one_case(index, case, base_cfg, suite_cfg, root, offline_dir, args):
    """
    单个 case 的 prepare：
        1. build_single_cfg
        2. 生成唯一 case_id
        3. 生成独立 .c
        4. 交叉编译独立 binary
        5. 返回 record
    """
    case_id = make_case_id(index, case)
    case_label = join_case_labels([case])

    src_dir = Path(offline_dir) / "src"
    bin_dir = Path(offline_dir) / "bin"

    src_path = src_dir / f"{case_id}.c"
    bin_path = bin_dir / case_id

    cfg = build_single_cfg(base_cfg, case, suite_cfg)

    knobs = build_knobs(root, artifact_stem=case_id)
    knobs["out_c"] = str(src_path)
    knobs["out_bin"] = str(bin_path)
    knobs = apply_knob_overrides(knobs, args)

    flat_cfg = build_offline_binary(cfg, knobs)

    return {
        "case_id": case_id,
        "suite": suite_cfg["name"],
        "case": case_label,
        "module": case["module"],
        "order_tag": "single",
        "modules": case_label,
        "params": case.get("params", {}),
        "src": f"src/{case_id}.c",
        "bin": f"bin/{case_id}",
        "log": f"logs/{case_id}.log",
        "flat_cfg": flat_cfg,
    }


def prepare(args):
    """
    阶段 1：本地执行。

    做：
        python 生成所有 .c
        多线程调交叉编译器编译 binary
        写 manifest.tsv
        写 case_index.json
        复制 run.sh

    不做：
        不上传
        不远程执行
        不下载
        不解析日志
    """
    root = PROJECT_ROOT
    suite_cfg = build_suite_cfg(args)
    base_cfg = build_base_cfg()

    offline_dir = (
        Path(args.offline_dir).resolve()
        if args.offline_dir
        else default_offline_dir(root)
    )

    (offline_dir / "src").mkdir(parents=True, exist_ok=True)
    (offline_dir / "bin").mkdir(parents=True, exist_ok=True)
    (offline_dir / "logs").mkdir(parents=True, exist_ok=True)

    print(f"[prepare] suite={suite_cfg['name']}")
    print(f"[prepare] cases={len(suite_cfg['cases'])}")
    print(f"[prepare] offline_dir={offline_dir}")
    print(f"[prepare] jobs={args.jobs}")

    records = []
    jobs = max(1, int(args.jobs))

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = [
            pool.submit(
                prepare_one_case,
                index,
                case,
                base_cfg,
                suite_cfg,
                root,
                offline_dir,
                args,
            )
            for index, case in enumerate(suite_cfg["cases"])
        ]

        for future in as_completed(futures):
            try:
                record = future.result()
            except Exception:
                traceback.print_exc()
                raise

            records.append(record)
            print(f"[OK] {record['case_id']}")

    records.sort(key=lambda item: item["case_id"])

    manifest_path = offline_dir / "manifest.tsv"
    case_index_path = offline_dir / "case_index.json"

    write_manifest_tsv(records, manifest_path)
    write_json(case_index_path, records)

    # if args.runner_sh:
    #     copied_runner = copy_runner_script(args.runner_sh, offline_dir)
    #     print(f"[prepare] copied run.sh -> {copied_runner}")

    print()
    print("[prepare] done")
    print(f"[prepare] upload this folder manually:")
    print(f"  {offline_dir}")
    print()
    print("[remote example]")
    print("  cd <uploaded_folder>")
    print("  CPU_MASK=f0 sh run.sh")
    print()
    print("[after remote run]")
    print("  download the folder back, then run:")
    print(f"  python3 {Path(__file__).name} analyze --offline-dir {offline_dir}")


def analyze_one_record(record, offline_dir, root):
    """
    单个 case 的 analyze：
        读取 logs/${case_id}.log
        解析 hiperf 输出
        生成 row
    """
    case_id = record["case_id"]
    log_path = Path(offline_dir) / record["log"]
    bin_path = Path(offline_dir) / record["bin"]

    if not log_path.exists():
        return {
            "case_id": case_id,
            "ok": False,
            "error": f"missing log: {log_path}",
            "row": {},
        }

    knobs = build_knobs(root, artifact_stem=case_id)
    knobs["out_bin"] = str(bin_path)

    try:
        row, raw_output = parse_run_log_file(
            log_path,
            knobs,
            cfg=record.get("flat_cfg"),
            binary_path=bin_path,
        )
    except Exception as exc:
        return {
            "case_id": case_id,
            "ok": False,
            "error": str(exc),
            "traceback": traceback.format_exc(),
            "row": {},
        }

    return {
        "case_id": case_id,
        "ok": True,
        "error": "",
        "row": row,
    }


def analyze(args):
    """
    阶段 3：本地执行。

    做：
        读取下载回来的 case_index.json
        读取 logs/*.log
        解析指标
        写 result.csv
        写 result.json

    不做：
        不生成 C
        不编译
        不远程运行
    """
    root = PROJECT_ROOT
    offline_dir = Path(args.offline_dir).resolve()

    case_index_path = offline_dir / "case_index.json"
    if not case_index_path.exists():
        raise FileNotFoundError(f"missing case_index.json: {case_index_path}")

    records = json.loads(case_index_path.read_text(encoding="utf-8"))

    csv_out = offline_dir / args.csv_name
    json_out = offline_dir / args.json_name

    if csv_out.exists() and not args.append:
        csv_out.unlink()

    headers = build_headers(METRIC_KEYS)
    json_rows = []

    print(f"[analyze] offline_dir={offline_dir}")
    print(f"[analyze] records={len(records)}")

    for record in records:
        result = analyze_one_record(record, offline_dir, root)

        base_info = {
            "case_id": record["case_id"],
            "suite": record["suite"],
            "case": record["case"],
            "module": record["module"],
            "params": record.get("params", {}),
            "src": record.get("src"),
            "bin": record.get("bin"),
            "log": record.get("log"),
            "ok": result["ok"],
            "error": result.get("error", ""),
        }

        row = result.get("row") or {}

        tagged_row = with_metric_separators(
            tag_row(
                row,
                record["suite"],
                record["case"],
                record["order_tag"],
                record["modules"],
            )
        )

        write_csv_row(csv_out, headers, tagged_row)

        json_rows.append(
            {
                **base_info,
                "row": tagged_row,
            }
        )

        if result["ok"]:
            print(f"[OK] {record['case_id']}")
        else:
            print(f"[FAIL] {record['case_id']}: {result.get('error', '')}")

    write_json(json_out, json_rows)

    print()
    print(f"[analyze] csv={csv_out}")
    print(f"[analyze] json={json_out}")


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Offline single-module pipeline: "
            "prepare locally, run manually on target, analyze locally."
        )
    )

    subparsers = parser.add_subparsers(dest="mode", required=True)

    prepare_parser = subparsers.add_parser(
        "prepare",
        help="Generate C files and cross-compile binaries locally.",
    )
    add_common_case_filter_args(prepare_parser)
    prepare_parser.add_argument("--output-dir", default="output")
    prepare_parser.add_argument(
        "--offline-dir",
        default="",
        help="Explicit offline output directory. If omitted, use output/<suite_stem>.",
    )
    prepare_parser.add_argument(
        "--jobs",
        type=int,
        default=8,
        help="Parallel local generate/compile jobs.",
    )
    prepare_parser.add_argument(
        "--cc",
        default="",
        help="Override compiler, e.g. aarch64-linux-gnu-gcc. Empty means build_knobs default.",
    )
    prepare_parser.add_argument(
        "--target",
        default="",
        help="Optional clang -target override.",
    )
    prepare_parser.add_argument(
        "--sysroot",
        default="",
        help="Optional compiler sysroot override.",
    )
    prepare_parser.add_argument(
        "--extra-cflags",
        default="",
        help="Comma-separated extra C flags appended to build_knobs extra_cflags.",
    )
    prepare_parser.add_argument(
        "--extra-ldflags",
        default="",
        help="Comma-separated extra LD flags appended to build_knobs extra_ldflags.",
    )
    prepare_parser.add_argument(
        "--runner-sh",
        default="run.sh",
        help="run.sh path. Relative path is resolved against this script directory.",
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Parse downloaded logs locally and write result CSV/JSON.",
    )
    analyze_parser.add_argument(
        "--offline-dir",
        required=True,
        help="Downloaded offline folder containing case_index.json and logs/.",
    )
    analyze_parser.add_argument(
        "--csv-name",
        default="result.csv",
    )
    analyze_parser.add_argument(
        "--json-name",
        default="result.json",
    )
    analyze_parser.add_argument(
        "--append",
        action="store_true",
        help="Append to existing CSV instead of replacing it.",
    )

    return parser.parse_args()


def add_common_case_filter_args(parser):
    """
    这些参数语义和原 run_single.py 保持一致：
        --modules 是过滤器
        --case-contains 是过滤器
        --max-cases 是过滤后的 round-robin cap
        --iters / --rounds 覆盖 suite run_defaults
    """
    parser.add_argument(
        "--modules",
        default="",
        help=(
            "Comma-separated module filter, e.g. "
            "hot_region_loop,fetch_amplifier,itlb,cold_block_sequence. "
            "Empty means keep all cases."
        ),
    )
    parser.add_argument(
        "--case-contains",
        default="",
        help="Only keep cases whose label contains this text.",
    )
    parser.add_argument(
        "--max-cases",
        type=int,
        default=None,
        help="Cap number of cases after filtering, round-robin by module.",
    )
    parser.add_argument(
        "--iters",
        type=int,
        default=None,
        help="Override run.iters for generated configs.",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=None,
        help="Override run.rounds for generated configs.",
    )


def main():
    args = parse_args()

    if args.mode == "prepare":
        prepare(args)
        return

    if args.mode == "analyze":
        analyze(args)
        return

    raise ValueError(f"unknown mode: {args.mode}")


if __name__ == "__main__":
    main()