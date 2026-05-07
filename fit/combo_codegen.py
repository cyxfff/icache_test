#!/usr/bin/env python3

from pathlib import Path

if __package__ in (None, "", "fit"):
    from modules.manager import SynthesisModuleManager
else:
    from ..modules.manager import SynthesisModuleManager


MODULES = SynthesisModuleManager()
FETCH_AMPLIFIER = getattr(MODULES, "fetch_amplifier", MODULES.cold_block_sequence)


def emit_instance_loop(reps: int, body: str) -> str:
    return (
        f"        for (uint32_t rep = 0; rep < {reps}u && !g_abort; ++rep) {{\n"
        f"            {body}\n"
        "        }\n"
    )


def generate_combo_source(instances, seed: int, default_iters: int = 10000) -> str:
    if not instances:
        raise ValueError("instances must not be empty")

    out = []
    out.append("#define _GNU_SOURCE\n")
    out.append("#include <errno.h>\n")
    out.append("#include <inttypes.h>\n")
    out.append("#include <signal.h>\n")
    out.append("#include <stdbool.h>\n")
    out.append("#include <stdint.h>\n")
    out.append("#include <stdio.h>\n")
    out.append("#include <stdlib.h>\n")
    out.append("#include <time.h>\n")
    out.append("#include <unistd.h>\n\n")
    out.append("typedef void (*bench_func_t)(void);\n\n")

    loop_bodies = []
    init_lines = []

    for index, instance in enumerate(instances):
        params = dict(instance["params"])
        module = instance["module"]
        prefix = f"inst_{index}_{module}"
        region_reps = max(1, int(params.get("region_reps", 1)))

        if module == "hot_region_loop":
            name = f"{prefix}_blob"
            size = int(params["size"])
            branch_pairs_per_unit = int(params.get("branch_pairs_per_unit", MODULES.hot_region_loop.DEFAULT_BRANCH_PAIRS_PER_UNIT))
            out.append(MODULES.hot_region_loop.emit_region_function(name, size, 64, branch_pairs_per_unit))
            runner_name = f"run_{prefix}_once"
            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {runner_name}(void) {{\n")
            out.append(f"    {name}();\n")
            out.append("}\n\n")
            loop_bodies.append(emit_instance_loop(region_reps, f"{runner_name}();"))
            continue

        if module == "fetch_amplifier":
            total_blocks = max(0, int(params["blocks"]))
            block_align = max(64, int(params.get("block_align", 64)))
            direct_run_len = FETCH_AMPLIFIER.normalize_direct_run_len(
                total_blocks,
                int(params.get("direct_run_len", 1)),
            )
            layout = str(params.get("layout", "linear"))
            physical_order = FETCH_AMPLIFIER.shuffled_block_order(
                total_blocks,
                block_align,
                seed ^ (0x3C6EF372 * (index + 1)),
                layout,
            )
            table_name = f"g_{prefix}_table"
            dispatch_name = f"dispatch_{prefix}_indirect"
            runner_name = f"run_{prefix}_once"

            out.append(f"static void *{table_name}[{total_blocks if total_blocks > 0 else 1}];\n")
            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {dispatch_name}(uint64_t idx) {{\n")
            out.append(f"    ((bench_func_t){table_name}[idx])();\n")
            out.append("}\n\n")

            fetch_slots_per_block = max(1, int(params.get("block_slots", 16)))
            for logical_id in physical_order:
                out.append(
                    FETCH_AMPLIFIER.emit_segment_function(
                        prefix,
                        logical_id,
                        total_blocks,
                        block_align,
                        dispatch_name,
                        direct_run_len,
                        int(params.get("branch_pairs_per_block", 0)),
                        fetch_slots_per_block,
                    )
                )

            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {runner_name}(void) {{\n")
            if total_blocks > 0:
                out.append(f"    ((bench_func_t){table_name}[0])();\n")
            out.append("}\n\n")

            for logical_id in range(total_blocks):
                init_lines.append(f"    {table_name}[{logical_id}] = (void *)&{prefix}_block_{logical_id};\n")
            if total_blocks == 0:
                init_lines.append(f"    {table_name}[0] = NULL;\n")

            loop_bodies.append(emit_instance_loop(region_reps, f"{runner_name}();"))
            continue

        if module == "cold_block_sequence":
            total_blocks = max(0, int(params["blocks"]))
            block_align = max(64, int(params.get("block_align", 64)))
            direct_run_len = MODULES.cold_block_sequence.normalize_direct_run_len(
                total_blocks,
                int(params.get("direct_run_len", 0)),
            )
            layout = str(params.get("layout", "in_page_shuffle"))
            physical_order = MODULES.cold_block_sequence.shuffled_block_order(
                total_blocks,
                block_align,
                seed ^ (0x1000193 * (index + 1)),
                layout,
            )
            table_name = f"g_{prefix}_table"
            dispatch_name = f"dispatch_{prefix}_indirect"
            runner_name = f"run_{prefix}_once"

            out.append(f"static void *{table_name}[{total_blocks if total_blocks > 0 else 1}];\n")
            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {dispatch_name}(uint64_t idx) {{\n")
            out.append(f"    ((bench_func_t){table_name}[idx])();\n")
            out.append("}\n\n")

            for logical_id in physical_order:
                out.append(
                    MODULES.cold_block_sequence.emit_segment_function(
                        prefix,
                        logical_id,
                        total_blocks,
                        block_align,
                        dispatch_name,
                        direct_run_len,
                    )
                )

            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {runner_name}(void) {{\n")
            if total_blocks > 0:
                out.append(f"    ((bench_func_t){table_name}[0])();\n")
            out.append("}\n\n")

            for logical_id in range(total_blocks):
                init_lines.append(f"    {table_name}[{logical_id}] = (void *)&{prefix}_block_{logical_id};\n")
            if total_blocks == 0:
                init_lines.append(f"    {table_name}[0] = NULL;\n")

            loop_bodies.append(emit_instance_loop(region_reps, f"{runner_name}();"))
            continue

        if module == "itlb":
            funcs = max(0, int(params["funcs"]))
            lines_per_page = MODULES.tlb_region.normalize_lines_per_page(int(params.get("lines_per_page", 1)))
            mode = str(params.get("mode", "chain"))
            direct_run_len = MODULES.tlb_region.normalize_direct_run_len(
                funcs,
                int(params.get("direct_run_len", 0)),
            )
            phys_order = MODULES.tlb_region.shuffled_itlb_phys_order(funcs, seed ^ (0x9E3779B1 + index))
            exec_order = MODULES.tlb_region.constrained_itlb_exec_order(
                phys_order,
                seed ^ (0x85EBCA77 + index),
                4,
            )
            next_map, chain_pos_map = MODULES.tlb_region.build_chain_maps(funcs, exec_order, mode)
            table_name = f"g_{prefix}_table"
            dispatch_name = f"dispatch_{prefix}_indirect"
            runner_name = f"run_{prefix}_once"

            out.append(f"static void *{table_name}[{funcs if funcs > 0 else 1}];\n")
            if mode == "chain" and direct_run_len > 0:
                out.append("__attribute__((used, noinline))\n")
                out.append(f"static void {dispatch_name}(uint64_t idx) {{\n")
                out.append(f"    ((bench_func_t){table_name}[idx])();\n")
                out.append("}\n\n")
                dispatcher_symbol = dispatch_name
            else:
                dispatcher_symbol = None

            for func_id in phys_order:
                out.append(
                    MODULES.tlb_region.emit_function(
                        prefix,
                        func_id,
                        next_map[func_id],
                        lines_per_page,
                        mode,
                        dispatcher_symbol,
                        direct_run_len,
                        chain_pos_map.get(func_id),
                    )
                )

            out.append("__attribute__((used, noinline))\n")
            out.append(f"static void {runner_name}(void) {{\n")
            if funcs > 0:
                out.append('    asm volatile("mov x9, xzr\\n\\t" "mov x10, xzr\\n\\t" ::: "x9", "x10", "cc", "memory");\n')
                if mode == "chain":
                    if exec_order:
                        out.append(f"    {prefix}_func_{exec_order[0]}();\n")
                else:
                    for func_id in range(funcs):
                        out.append(f"    {prefix}_func_{func_id}();\n")
            out.append("}\n\n")

            for func_id in range(funcs):
                init_lines.append(f"    {table_name}[{func_id}] = (void *)&{prefix}_func_{func_id};\n")
            if funcs == 0:
                init_lines.append(f"    {table_name}[0] = NULL;\n")

            loop_bodies.append(emit_instance_loop(region_reps, f"{runner_name}();"))
            continue

        raise ValueError(f"unsupported combo module: {module}")

    out.append("static volatile sig_atomic_t g_start = 0;\n")
    out.append("static volatile sig_atomic_t g_abort = 0;\n\n")
    out.append(
        "static void on_start(int signo) {\n"
        "    (void)signo;\n"
        "    g_start = 1;\n"
        "}\n\n"
    )
    out.append(
        "static void on_abort(int signo) {\n"
        "    (void)signo;\n"
        "    g_abort = 1;\n"
        "}\n\n"
    )
    out.append(
        "static uint64_t parse_u64(const char *text, uint64_t fallback) {\n"
        "    if (!text || !*text) return fallback;\n"
        "    errno = 0;\n"
        "    char *end = NULL;\n"
        "    unsigned long long value = strtoull(text, &end, 10);\n"
        "    if (errno != 0 || !end || *end != '\\0') {\n"
        "        return fallback;\n"
        "    }\n"
        "    return (uint64_t)value;\n"
        "}\n\n"
    )
    out.append(
        "static void wait_for_start_signal(void) {\n"
        "    sigset_t mask;\n"
        "    sigemptyset(&mask);\n"
        "    while (!g_start && !g_abort) {\n"
        "        sigsuspend(&mask);\n"
        "    }\n"
        "}\n\n"
    )

    out.append("int main(int argc, char **argv) {\n")
    out.append("    struct sigaction sa_start;\n")
    out.append("    struct sigaction sa_abort;\n")
    out.append("    sa_start.sa_handler = on_start;\n")
    out.append("    sigemptyset(&sa_start.sa_mask);\n")
    out.append("    sa_start.sa_flags = 0;\n")
    out.append("    sa_abort.sa_handler = on_abort;\n")
    out.append("    sigemptyset(&sa_abort.sa_mask);\n")
    out.append("    sa_abort.sa_flags = 0;\n")
    out.append("    sigaction(SIGUSR1, &sa_start, NULL);\n")
    out.append("    sigaction(SIGTERM, &sa_abort, NULL);\n")
    out.append("    sigaction(SIGINT, &sa_abort, NULL);\n\n")
    out.append(f"    uint64_t iters = {int(default_iters)}ull;\n")
    out.append("    if (argc > 1) iters = parse_u64(argv[1], iters);\n")
    out.append("    if (iters == 0) iters = 1;\n\n")

    for line in init_lines:
        out.append(line)
    if init_lines:
        out.append("\n")

    out.append("    fflush(stdout);\n")
    out.append('    puts("PROXYBENCH_READY");\n')
    out.append("    fflush(stdout);\n")
    out.append("    wait_for_start_signal();\n")
    out.append("    struct timespec bench_start;\n")
    out.append("    struct timespec bench_end;\n")
    out.append("    clock_gettime(CLOCK_MONOTONIC, &bench_start);\n")
    out.append("    uint64_t completed_iters = 0;\n")
    out.append("    while (!g_abort && completed_iters < iters) {\n")
    for body in loop_bodies:
        out.append(body)
    out.append("        ++completed_iters;\n")
    out.append("    }\n\n")
    out.append("    clock_gettime(CLOCK_MONOTONIC, &bench_end);\n")
    out.append(
        "    double bench_seconds = (double)(bench_end.tv_sec - bench_start.tv_sec) + "
        "1e-9 * (double)(bench_end.tv_nsec - bench_start.tv_nsec);\n"
    )
    out.append('    printf("completed_iters=%" PRIu64 "\\n", completed_iters);\n')
    out.append('    printf("bench_seconds=%.9f\\n", bench_seconds);\n')
    out.append("    fflush(stdout);\n")
    out.append("    return g_abort ? 130 : 0;\n")
    out.append("}\n")
    return "".join(out)


def write_combo_source(out_path, source: str) -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="ascii") as handle:
        handle.write(source)
