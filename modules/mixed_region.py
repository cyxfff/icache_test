import random
from math import gcd
from typing import List


class MixedRegionBuilder:
    CACHE_LINE_BYTES = 64
    PAGE_BYTES = 4096
    NODE_BYTES = 8
    UNIT_INSNS = 16
    FIXED_INSNS = 2
    INSTR_FAMILY_CHOICES = (
        "hot_loop",
        "block_chain",
        "fetch_amplifier",
        "itlb_walk",
        "call_ret",
        "indirect_target",
    )
    DATA_MODE_CHOICES = (
        "linear",
        "node_stride",
        "line_stride",
        "page_stride",
        "line_shuffle",
        "random",
        # Legacy aliases kept so old CSV/config rows still build.
        "page_shuffle",
        "cross_page",
        "indirect",
    )
    DATA_MODE_ALIASES = {
        "line_stride": "node_stride",
        "page_shuffle": "line_shuffle",
        "cross_page": "page_stride",
        "indirect": "random",
    }

    @classmethod
    def normalize_size_bytes(cls, total_bytes: int) -> int:
        if total_bytes <= 0:
            return 0
        units = max(1, (int(total_bytes) + cls.CACHE_LINE_BYTES - 1) // cls.CACHE_LINE_BYTES)
        return units * cls.CACHE_LINE_BYTES

    @classmethod
    def normalize_pages(cls, page_count: int) -> int:
        return max(0, int(page_count))

    @classmethod
    def normalize_lines_per_page(cls, lines_per_page: int) -> int:
        return cls.normalize_nodes_per_page(lines_per_page)

    @classmethod
    def normalize_nodes_per_page(cls, nodes_per_page: int) -> int:
        return max(1, min(cls.PAGE_BYTES // cls.NODE_BYTES, int(nodes_per_page)))

    @staticmethod
    def normalize_stride(stride: int) -> int:
        return max(1, int(stride))

    @classmethod
    def normalize_cycle_stride(cls, item_count: int, stride: int) -> int:
        if item_count <= 1:
            return 1
        candidate = cls.normalize_stride(stride) % item_count
        if candidate == 0:
            candidate = 1
        while gcd(candidate, item_count) != 1:
            candidate += 1
            if candidate >= item_count:
                candidate = 1
        return candidate

    @classmethod
    def normalize_ldr_count_per_unit(cls, ldr_count_per_unit: int) -> int:
        max_ldr_count = max(0, cls.UNIT_INSNS - cls.FIXED_INSNS)
        return max(0, min(max_ldr_count, int(ldr_count_per_unit)))

    @classmethod
    def normalize_data_mode(cls, data_mode: str) -> str:
        mode = str(data_mode)
        if mode not in cls.DATA_MODE_CHOICES:
            raise ValueError(f"unsupported mixed-region data mode: {mode}")
        return cls.DATA_MODE_ALIASES.get(mode, mode)

    @classmethod
    def normalize_instr_family(cls, instr_family: str) -> str:
        family = str(instr_family)
        if family not in cls.INSTR_FAMILY_CHOICES:
            raise ValueError(f"unsupported mixed-region instruction family: {family!r}; choose from {cls.INSTR_FAMILY_CHOICES}")
        return family

    def selected_node_offsets(self, nodes_per_page: int) -> List[int]:
        nodes_per_page = self.normalize_nodes_per_page(nodes_per_page)
        page_nodes = self.PAGE_BYTES // self.NODE_BYTES
        return [
            ((idx * page_nodes) // nodes_per_page) * self.NODE_BYTES
            for idx in range(nodes_per_page)
        ]

    def build_pointer_offsets(
        self,
        page_count: int,
        lines_per_page: int,
        data_mode: str,
        seed: int,
        stride_lines: int = 1,
        stride_pages: int = 1,
        nodes_per_page: int = None,
        stride_nodes: int = None,
    ) -> List[int]:
        page_count = self.normalize_pages(page_count)
        nodes_per_page = self.normalize_nodes_per_page(
            lines_per_page if nodes_per_page is None else nodes_per_page
        )
        data_mode = self.normalize_data_mode(data_mode)
        if page_count <= 0:
            return []

        rng = random.Random(seed ^ 0x6C8E9CF5)
        node_offsets = self.selected_node_offsets(nodes_per_page)
        all_offsets = [
            page_idx * self.PAGE_BYTES + node_offset
            for page_idx in range(page_count)
            for node_offset in node_offsets
        ]
        if data_mode == "linear":
            return all_offsets

        if data_mode == "line_shuffle":
            offsets: List[int] = []
            for page_idx in range(page_count):
                node_order = list(node_offsets)
                rng.shuffle(node_order)
                base = page_idx * self.PAGE_BYTES
                for node_offset in node_order:
                    offsets.append(base + node_offset)
            return offsets

        if data_mode == "node_stride":
            step = self.normalize_cycle_stride(
                len(all_offsets),
                stride_lines if stride_nodes is None else stride_nodes,
            )
            return [all_offsets[(idx * step) % len(all_offsets)] for idx in range(len(all_offsets))]

        if data_mode == "page_stride":
            page_step = self.normalize_cycle_stride(page_count, stride_pages)
            page_order = [(idx * page_step) % page_count for idx in range(page_count)]
            offsets: List[int] = []
            for node_offset in node_offsets:
                for page_idx in page_order:
                    offsets.append(page_idx * self.PAGE_BYTES + node_offset)
            return offsets

        rng.shuffle(all_offsets)
        return all_offsets

    @classmethod
    def emit_storage(cls, prefix: str, pool_bytes_macro: str, align: int = 4096) -> str:
        return (
            f"static uint8_t *g_{prefix}_pool = NULL;\n"
            f"static uintptr_t g_{prefix}_cursor = 0;\n"
            f"static uint64_t g_{prefix}_sink = 0;\n\n"
        )

    @staticmethod
    def emit_init_function(prefix: str, offsets_symbol: str, count_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void init_{prefix}_pool(void) {{\n"
            f"    if ({count_macro} == 0) {{\n"
            f"        g_{prefix}_cursor = 0;\n"
            "        return;\n"
            "    }\n"
            f"    for (uint32_t idx = 0; idx < {count_macro}; ++idx) {{\n"
            f"        uint32_t cur = {offsets_symbol}[idx];\n"
            f"        uint32_t nxt = {offsets_symbol}[(idx + 1) % {count_macro}];\n"
            f"        *(uintptr_t *)(g_{prefix}_pool + cur) = (uintptr_t)(g_{prefix}_pool + nxt);\n"
            "    }\n"
            f"    g_{prefix}_cursor = (uintptr_t)(g_{prefix}_pool + {offsets_symbol}[0]);\n"
            "}\n\n"
        )

    @classmethod
    def _ldr_positions(cls, ldr_count_per_unit: int) -> List[int]:
        filler_slots = cls.UNIT_INSNS - cls.FIXED_INSNS
        ldr_count = cls.normalize_ldr_count_per_unit(ldr_count_per_unit)
        if ldr_count == 0:
            return []
        return [
            ((slot_idx + 1) * filler_slots) // ldr_count
            for slot_idx in range(ldr_count)
        ]

    @classmethod
    def emit_unit_body(cls, ldr_count_per_unit: int) -> str:
        ldr_count = cls.normalize_ldr_count_per_unit(ldr_count_per_unit)
        filler_slots = cls.UNIT_INSNS - cls.FIXED_INSNS
        ldr_positions = set(cls._ldr_positions(ldr_count))
        out = []
        out.append('        "add x9, x9, #1\\n\\t"\n')
        out.append('        "eor x10, x10, x9\\n\\t"\n')
        if ldr_count == 0:
            out.append(f'        ".rept {filler_slots}\\n\\t"\n')
            out.append('        "nop\\n\\t"\n')
            out.append('        ".endr\\n\\t"\n')
            return "".join(out)

        pending_nops = 0
        for slot_idx in range(1, filler_slots + 1):
            if slot_idx not in ldr_positions:
                pending_nops += 1
                continue

            if pending_nops > 0:
                out.append(f'        ".rept {pending_nops}\\n\\t"\n')
                out.append('        "nop\\n\\t"\n')
                out.append('        ".endr\\n\\t"\n')
                pending_nops = 0
            out.append('        "ldr x11, [x11]\\n\\t"\n')

        if pending_nops > 0:
            out.append(f'        ".rept {pending_nops}\\n\\t"\n')
            out.append('        "nop\\n\\t"\n')
            out.append('        ".endr\\n\\t"\n')
        return "".join(out)

    @classmethod
    def emit_region_function(cls, prefix: str, total_bytes: int, ldr_count_per_unit: int, align: int = 64) -> str:
        total_bytes = cls.normalize_size_bytes(total_bytes)
        if total_bytes <= 0:
            return ""

        unit_count = total_bytes // cls.CACHE_LINE_BYTES
        out = [
            "#if defined(__aarch64__)\n",
            f"__attribute__((used, noinline, aligned({align})))\n",
            f"static void {prefix}_kernel(void) {{\n",
            f"    uintptr_t cursor = g_{prefix}_cursor;\n",
            "    if (cursor == 0) return;\n",
            "    asm volatile(\n",
            '        "mov x11, %[cursor]\\n\\t"\n',
        ]
        for _ in range(unit_count):
            out.append(cls.emit_unit_body(ldr_count_per_unit))
        out.extend(
            [
                '        "mov %[cursor], x11\\n\\t"\n',
                "        : [cursor] \"+r\"(cursor)\n",
                "        :\n",
                '        : "x9", "x10", "x11", "cc", "memory");\n',
                f"    g_{prefix}_cursor = cursor;\n",
                "}\n\n",
                "#else\n",
                "__attribute__((used, noinline))\n",
                f"static void {prefix}_kernel(void) {{\n",
                f"    uintptr_t cursor = g_{prefix}_cursor;\n"
                "    if (cursor == 0) return;\n"
                "    uint64_t acc = g_"
                f"{prefix}"
                "_sink;\n"
                f"    for (uint32_t unit = 0; unit < {unit_count}u; ++unit) {{\n"
                "        acc += (uint64_t)(unit + 1u);\n"
                "        acc ^= acc << 7;\n",
            ]
        )
        ldr_count = cls.normalize_ldr_count_per_unit(ldr_count_per_unit)
        if ldr_count == 0:
            out.append("        (void)acc;\n")
        else:
            for _ in range(ldr_count):
                out.append("        cursor = *(uintptr_t *)cursor;\n")
        out.extend(
            [
                "    }\n"
                f"    g_{prefix}_cursor = cursor;\n"
                f"    g_{prefix}_sink = acc;\n"
                "}\n",
                "#endif\n\n",
            ]
        )
        return "".join(out)

    @classmethod
    def emit_pointer_burst_function(cls, prefix: str, load_count: int) -> str:
        load_count = max(0, int(load_count))
        if load_count <= 0:
            return ""

        out = [
            "#if defined(__aarch64__)\n",
            "__attribute__((used, noinline))\n",
            f"static void {prefix}_burst(void) {{\n",
            f"    uintptr_t cursor = g_{prefix}_cursor;\n",
            "    if (cursor == 0) return;\n",
            "    asm volatile(\n",
            '        "mov x11, %[cursor]\\n\\t"\n',
        ]
        for _ in range(load_count):
            out.append('        "ldr x11, [x11]\\n\\t"\n')
        out.extend(
            [
                '        "mov %[cursor], x11\\n\\t"\n',
                "        : [cursor] \"+r\"(cursor)\n",
                "        :\n",
                '        : "x11", "memory");\n',
                f"    g_{prefix}_cursor = cursor;\n",
                "}\n\n",
                "#else\n",
                "__attribute__((used, noinline))\n",
                f"static void {prefix}_burst(void) {{\n",
                f"    uintptr_t cursor = g_{prefix}_cursor;\n"
                "    if (cursor == 0) return;\n"
                f"    for (uint32_t idx = 0; idx < {load_count}u; ++idx) {{\n"
                "        cursor = *(uintptr_t *)cursor;\n"
                "    }\n"
                f"    g_{prefix}_cursor = cursor;\n"
                "}\n",
                "#endif\n\n",
            ]
        )
        return "".join(out)
