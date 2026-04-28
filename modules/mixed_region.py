import random
from typing import List


class MixedRegionBuilder:
    CACHE_LINE_BYTES = 64
    PAGE_BYTES = 4096
    UNIT_INSNS = 16
    FIXED_INSNS = 2
    DATA_MODE_CHOICES = ("linear", "page_shuffle", "cross_page", "indirect")

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
        return max(1, min(cls.PAGE_BYTES // cls.CACHE_LINE_BYTES, int(lines_per_page)))

    @classmethod
    def normalize_ldr_count_per_unit(cls, ldr_count_per_unit: int) -> int:
        max_ldr_count = max(0, cls.UNIT_INSNS - cls.FIXED_INSNS)
        return max(0, min(max_ldr_count, int(ldr_count_per_unit)))

    @classmethod
    def normalize_data_mode(cls, data_mode: str) -> str:
        mode = str(data_mode)
        if mode not in cls.DATA_MODE_CHOICES:
            raise ValueError(f"unsupported mixed-region data mode: {mode}")
        return mode

    def build_pointer_offsets(self, page_count: int, lines_per_page: int, data_mode: str, seed: int) -> List[int]:
        page_count = self.normalize_pages(page_count)
        lines_per_page = self.normalize_lines_per_page(lines_per_page)
        data_mode = self.normalize_data_mode(data_mode)
        if page_count <= 0:
            return []

        rng = random.Random(seed ^ 0x6C8E9CF5)
        all_offsets = [
            page_index * self.PAGE_BYTES + line_index * self.CACHE_LINE_BYTES
            for page_index in range(page_count)
            for line_index in range(lines_per_page)
        ]
        if data_mode == "linear":
            return all_offsets

        if data_mode == "page_shuffle":
            offsets: List[int] = []
            for page_index in range(page_count):
                line_order = list(range(lines_per_page))
                rng.shuffle(line_order)
                base = page_index * self.PAGE_BYTES
                for line_index in line_order:
                    offsets.append(base + line_index * self.CACHE_LINE_BYTES)
            return offsets

        if data_mode == "cross_page":
            page_order = list(range(page_count))
            rng.shuffle(page_order)
            offsets = []
            for line_index in range(lines_per_page):
                for page_index in page_order:
                    offsets.append(page_index * self.PAGE_BYTES + line_index * self.CACHE_LINE_BYTES)
            return offsets

        rng.shuffle(all_offsets)
        return all_offsets

    @classmethod
    def emit_storage(cls, prefix: str, pool_bytes_macro: str, align: int = 4096) -> str:
        return (
            f"static uint8_t g_{prefix}_pool[{pool_bytes_macro} > 0 ? {pool_bytes_macro} : 64u] "
            f"__attribute__((aligned({align})));\n"
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
            f"        *(uint64_t *)(g_{prefix}_pool + cur + 8u) = (uint64_t)(cur ^ nxt ^ idx);\n"
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
            ((slot + 1) * filler_slots) // ldr_count
            for slot in range(ldr_count)
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
        for slot in range(1, filler_slots + 1):
            if slot not in ldr_positions:
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
