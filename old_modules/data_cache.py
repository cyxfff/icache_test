import math
import random
from typing import List


class DataCacheBuilder:
    CACHE_LINE_BYTES = 64
    PAGE_BYTES = 4096

    @classmethod
    def normalize_size_bytes(cls, total_bytes: int) -> int:
        if total_bytes <= 0:
            return 0
        lines = max(1, (int(total_bytes) + cls.CACHE_LINE_BYTES - 1) // cls.CACHE_LINE_BYTES)
        return lines * cls.CACHE_LINE_BYTES

    @staticmethod
    def normalize_stride_bytes(total_bytes: int, stride_bytes: int) -> int:
        if total_bytes <= 0:
            return 0
        stride = max(8, int(stride_bytes))
        stride = ((stride + 7) // 8) * 8
        return min(stride, max(8, int(total_bytes)))

    @staticmethod
    def normalize_page_count(page_count: int) -> int:
        return max(0, int(page_count))

    @staticmethod
    def normalize_access_count(access_count: int) -> int:
        return max(0, int(access_count))

    @staticmethod
    def normalize_word_stride_bytes(stride_bytes: int) -> int:
        stride = max(4, int(stride_bytes))
        return ((stride + 3) // 4) * 4

    @classmethod
    def normalize_lines_per_page(cls, lines_per_page: int) -> int:
        return max(1, min(cls.PAGE_BYTES // cls.CACHE_LINE_BYTES, int(lines_per_page)))

    @classmethod
    def normalize_line_index(cls, line_index: int) -> int:
        return max(0, min((cls.PAGE_BYTES // cls.CACHE_LINE_BYTES) - 1, int(line_index)))

    @staticmethod
    def normalize_cycle_stride(element_count: int, stride: int) -> int:
        if element_count <= 1:
            return 1

        value = max(1, int(stride)) % element_count
        if value == 0:
            value = 1

        while math.gcd(value, element_count) != 1:
            value += 1
            if value >= element_count:
                value = 1
                break
        return value

    def build_pointer_chase_offsets(self, page_count: int, lines_per_page: int, seed: int) -> List[int]:
        page_count = self.normalize_page_count(page_count)
        lines_per_page = self.normalize_lines_per_page(lines_per_page)
        if page_count <= 0:
            return []

        rng = random.Random(seed ^ 0xC6A4A793)
        page_order = list(range(page_count))
        rng.shuffle(page_order)

        offsets: List[int] = []
        for page_index in page_order:
            line_order = list(range(lines_per_page))
            rng.shuffle(line_order)
            base = page_index * self.PAGE_BYTES
            for line_index in line_order:
                offsets.append(base + line_index * self.CACHE_LINE_BYTES)
        return offsets

    def build_page_stride_offsets(self, page_count: int, page_stride: int, line_index: int, seed: int) -> List[int]:
        page_count = self.normalize_page_count(page_count)
        line_index = self.normalize_line_index(line_index)
        if page_count <= 0:
            return []

        page_stride = self.normalize_cycle_stride(page_count, page_stride)
        current_page = seed % page_count
        offsets: List[int] = []
        for _ in range(page_count):
            offsets.append(current_page * self.PAGE_BYTES + line_index * self.CACHE_LINE_BYTES)
            current_page = (current_page + page_stride) % page_count
        return offsets

    def build_stride_offsets(self, access_count: int, stride_bytes: int) -> List[int]:
        access_count = self.normalize_access_count(access_count)
        stride_bytes = self.normalize_word_stride_bytes(stride_bytes)
        return [index * stride_bytes for index in range(access_count)]

    def build_tlb_indirect_offsets(self, page_count: int, line_index: int, seed: int) -> List[int]:
        page_count = self.normalize_page_count(page_count)
        line_index = self.normalize_line_index(line_index)
        if page_count <= 0:
            return []

        rng = random.Random(seed ^ 0x71B54A32)
        page_order = list(range(page_count))
        rng.shuffle(page_order)
        return [page_id * self.PAGE_BYTES + line_index * self.CACHE_LINE_BYTES for page_id in page_order]

    @staticmethod
    def emit_stream_storage(prefix: str, size_macro: str, align: int = 64) -> str:
        return (
            f"static uint8_t *g_{prefix}_buf = NULL;\n"
            f"static uint64_t g_{prefix}_sink = 0;\n\n"
        )

    @staticmethod
    def emit_stream_init_function(prefix: str, size_macro: str, seed_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void init_{prefix}_buffer(void) {{\n"
            f"    for (uint32_t idx = 0; idx < {size_macro}; ++idx) {{\n"
            f"        g_{prefix}_buf[idx] = (uint8_t)(((idx * 131u) + {seed_macro}) & 0xFFu);\n"
            "    }\n"
            "}\n\n"
        )

    @staticmethod
    def emit_stream_function(prefix: str, size_macro: str, stride_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void {prefix}_kernel(void) {{\n"
            f"    if ({size_macro} == 0) return;\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    for (uint32_t offset = 0; offset < {size_macro}; offset += {stride_macro}) {{\n"
            f"        acc += *(const volatile uint64_t *)(g_{prefix}_buf + offset);\n"
            "    }\n"
            f"    g_{prefix}_sink = acc;\n"
            "}\n\n"
        )

    @staticmethod
    def emit_offset_gather_function(prefix: str, offsets_symbol: str, count_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void {prefix}_kernel(void) {{\n"
            f"    if ({count_macro} == 0) return;\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    for (uint32_t idx = 0; idx < {count_macro}; ++idx) {{\n"
            f"        uint32_t offset = {offsets_symbol}[idx];\n"
            f"        acc += *(const volatile uint64_t *)(g_{prefix}_buf + offset);\n"
            "    }\n"
            f"    g_{prefix}_sink = acc;\n"
            "}\n\n"
        )

    @staticmethod
    def emit_offset_cycle_function(prefix: str, offsets_symbol: str, count_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void {prefix}_kernel(void) {{\n"
            f"    if ({count_macro} == 0) return;\n"
            "#if defined(__aarch64__)\n"
            f"    const uint8_t *base = g_{prefix}_buf;\n"
            f"    const uint32_t *offsets = {offsets_symbol};\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    uint64_t count = (uint64_t){count_macro};\n"
            "    asm volatile(\n"
            '        "mov x9, xzr\\n\\t"\n'
            '        "mov x10, %[acc]\\n\\t"\n'
            '        "1:\\n\\t"\n'
            '        "ldr w11, [%[offsets], x9, lsl #2]\\n\\t"\n'
            '        "ldr w12, [%[base], x11]\\n\\t"\n'
            '        "add x10, x10, x12\\n\\t"\n'
            '        "add x9, x9, #1\\n\\t"\n'
            '        "cmp x9, %[count]\\n\\t"\n'
            '        "b.lo 1b\\n\\t"\n'
            '        "mov %[acc], x10\\n\\t"\n'
            "        : [acc] \"+r\"(acc)\n"
            "        : [base] \"r\"(base), [offsets] \"r\"(offsets), [count] \"r\"(count)\n"
            '        : "x9", "x10", "x11", "x12", "cc", "memory");\n'
            f"    g_{prefix}_sink = acc;\n"
            "#else\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    for (uint32_t idx = 0; idx < {count_macro}; ++idx) {{\n"
            f"        uint32_t offset = {offsets_symbol}[idx];\n"
            f"        acc += *(const volatile uint32_t *)(g_{prefix}_buf + offset);\n"
            "    }\n"
            f"    g_{prefix}_sink = acc;\n"
            "#endif\n"
            "}\n\n"
        )

    @staticmethod
    def emit_pointer_chase_storage(prefix: str, pool_bytes_macro: str, align: int = 4096) -> str:
        return (
            f"static uint8_t *g_{prefix}_pool = NULL;\n"
            f"static uint32_t g_{prefix}_cursor = 0;\n"
            f"static uint64_t g_{prefix}_sink = 0;\n\n"
        )

    @staticmethod
    def emit_pointer_chase_init_function(prefix: str, offsets_symbol: str, count_macro: str, seed_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void init_{prefix}_pool(void) {{\n"
            f"    if ({count_macro} == 0) return;\n"
            f"    for (uint32_t idx = 0; idx < {count_macro}; ++idx) {{\n"
            f"        uint32_t cur = {offsets_symbol}[idx];\n"
            f"        uint32_t nxt = {offsets_symbol}[(idx + 1) % {count_macro}];\n"
            f"        *(uint32_t *)(g_{prefix}_pool + cur) = nxt;\n"
            f"        *(uint64_t *)(g_{prefix}_pool + cur + 8u) = "
            f"(uint64_t)(cur ^ nxt ^ {seed_macro}) + (uint64_t)(idx + 1u);\n"
            "    }\n"
            f"    g_{prefix}_cursor = {offsets_symbol}[0];\n"
            "}\n\n"
        )

    @staticmethod
    def emit_pointer_chase_function(prefix: str, count_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void {prefix}_kernel(void) {{\n"
            f"    if ({count_macro} == 0) return;\n"
            f"    uint32_t offset = g_{prefix}_cursor;\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    for (uint32_t step = 0; step < {count_macro}; ++step) {{\n"
            f"        offset = *(volatile uint32_t *)(g_{prefix}_pool + offset);\n"
            f"        acc += *(volatile uint64_t *)(g_{prefix}_pool + offset + 8u);\n"
            "    }\n"
            f"    g_{prefix}_cursor = offset;\n"
            f"    g_{prefix}_sink = acc;\n"
            "}\n\n"
        )

    @staticmethod
    def emit_indirect_gather_storage(prefix: str, pool_bytes_macro: str, count_macro: str, align: int = 4096) -> str:
        return (
            f"static uint8_t *g_{prefix}_pool = NULL;\n"
            f"static uint32_t g_{prefix}_next[{count_macro} > 0 ? {count_macro} : 1u];\n"
            f"static uint32_t g_{prefix}_offsets[{count_macro} > 0 ? {count_macro} : 1u];\n"
            f"static uint32_t g_{prefix}_cursor = 0;\n"
            f"static uint64_t g_{prefix}_sink = 0;\n\n"
        )

    @staticmethod
    def emit_indirect_gather_init_function(
        prefix: str,
        offsets_symbol: str,
        count_macro: str,
        pool_bytes_macro: str,
        index_stride_macro: str,
        seed_macro: str,
    ) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void init_{prefix}_pool(void) {{\n"
            f"    for (uint32_t idx = 0; idx < {pool_bytes_macro}; ++idx) {{\n"
            f"        g_{prefix}_pool[idx] = (uint8_t)(((idx * 29u) + {seed_macro}) & 0xFFu);\n"
            "    }\n"
            f"    if ({count_macro} == 0) return;\n"
            f"    for (uint32_t idx = 0; idx < {count_macro}; ++idx) {{\n"
            f"        uint32_t offset = {offsets_symbol}[idx];\n"
            f"        g_{prefix}_offsets[idx] = offset;\n"
            f"        g_{prefix}_next[idx] = (idx + {index_stride_macro}) % {count_macro};\n"
            f"        *(uint64_t *)(g_{prefix}_pool + offset + 8u) = "
            f"(uint64_t)(offset ^ {seed_macro}) + (uint64_t)(idx + 1u);\n"
            "    }\n"
            f"    g_{prefix}_cursor = 0;\n"
            "}\n\n"
        )

    @staticmethod
    def emit_indirect_gather_function(prefix: str, count_macro: str) -> str:
        return (
            "__attribute__((used, noinline))\n"
            f"static void {prefix}_kernel(void) {{\n"
            f"    if ({count_macro} == 0) return;\n"
            f"    uint32_t idx = g_{prefix}_cursor;\n"
            f"    uint64_t acc = g_{prefix}_sink;\n"
            f"    for (uint32_t step = 0; step < {count_macro}; ++step) {{\n"
            f"        idx = *(volatile uint32_t *)(g_{prefix}_next + idx);\n"
            f"        uint32_t offset = *(volatile uint32_t *)(g_{prefix}_offsets + idx);\n"
            f"        acc += *(volatile uint64_t *)(g_{prefix}_pool + offset + 8u);\n"
            "    }\n"
            f"    g_{prefix}_cursor = idx;\n"
            f"    g_{prefix}_sink = acc;\n"
            "}\n\n"
        )
