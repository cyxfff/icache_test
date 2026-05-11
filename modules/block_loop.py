import random
from typing import List, Optional


class BlockLoopBuilder:
    @staticmethod
    def bit_reversal_permutation(count: int) -> List[int]:
        if count <= 1:
            return list(range(count))

        width = (count - 1).bit_length()
        order = []
        for idx in range(count):
            reversed_bits = 0
            value = idx
            for _ in range(width):
                reversed_bits = (reversed_bits << 1) | (value & 1)
                value >>= 1
            order.append(reversed_bits)
        return order

    def shuffled_block_order(self, total_blocks: int, block_align: int, seed: int, layout: str) -> List[int]:
        if total_blocks <= 0:
            return []

        if layout == "linear":
            return list(range(total_blocks))

        rng = random.Random(seed)

        if layout == "full_shuffle":
            order = list(range(total_blocks))
            rng.shuffle(order)
            return order

        if layout not in ("page_shuffle", "in_page_shuffle"):
            raise ValueError(f"unknown layout={layout}")

        if block_align <= 0 or 4096 % block_align != 0:
            raise ValueError(
                f"block_align={block_align} must be a positive divisor of 4096 when layout={layout}"
            )

        blocks_per_page = 4096 // block_align
        page_count = (total_blocks + blocks_per_page - 1) // blocks_per_page
        page_order = list(range(page_count))
        rng.shuffle(page_order)
        line_order = self.bit_reversal_permutation(blocks_per_page)

        order: List[int] = []
        for page_idx in page_order:
            start = page_idx * blocks_per_page
            end = min(start + blocks_per_page, total_blocks)
            for slot_idx in line_order:
                block_id = start + slot_idx
                if block_id < end:
                    order.append(block_id)

        return order

    @staticmethod
    def normalize_direct_run_len(total_blocks: int, direct_run_len: int) -> int:
        if total_blocks <= 0:
            return 0
        return max(1, min(direct_run_len, max(1, total_blocks)))

    @staticmethod
    def count_indirect_blocks(total_blocks: int, direct_run_len: int) -> int:
        if total_blocks <= 1:
            return 0
        return sum(
            1
            for logical_id in range(total_blocks - 1)
            if direct_run_len <= 1 or ((logical_id + 1) % direct_run_len == 0)
        )

    @staticmethod
    def nop_fill_asm(count: int) -> str:
        if count <= 0:
            return ""
        return (
            f'        ".rept {count}\\n\\t"\n'
            '        "nop\\n\\t"\n'
            '        ".endr\\n\\t"\n'
        )

    @staticmethod
    def branch_pair_fill_asm(count: int) -> str:
        if count <= 0:
            return ""
        out = []
        for label_idx in range(1, count + 1):
            out.append('        "cmp x9, x9\\n\\t"\n')
            out.append(f'        "b.ne {label_idx}f\\n\\t"\n')
            out.append(f'        "{label_idx}:\\n\\t"\n')
        return "".join(out)

    @staticmethod
    def mov_imm64_asm(reg: str, value: int) -> List[str]:
        parts = []
        wrote = False
        for shift in (0, 16, 32, 48):
            chunk = (value >> shift) & 0xFFFF
            if not wrote:
                if chunk != 0 or shift == 48:
                    if shift == 0:
                        parts.append(f'        "movz {reg}, #{chunk}\\n\\t"\n')
                    else:
                        parts.append(f'        "movz {reg}, #{chunk}, lsl #{shift}\\n\\t"\n')
                    wrote = True
            elif chunk != 0:
                parts.append(f'        "movk {reg}, #{chunk}, lsl #{shift}\\n\\t"\n')
        if not parts:
            parts.append(f'        "movz {reg}, #0\\n\\t"\n')
        return parts

    def emit_segment_function(
        self,
        prefix: str,
        logical_id: int,
        total_blocks: int,
        block_align: int,
        dispatcher_symbol: Optional[str],
        direct_run_len: int,
        branch_pairs_per_block: int = 0,
        slots_per_block: int = 16,
    ) -> str:
        is_last = logical_id == total_blocks - 1
        target_symbol = None if is_last else f"{prefix}_block_{logical_id + 1}"
        use_indirect = (
            dispatcher_symbol is not None
            and not is_last
            and (direct_run_len <= 1 or ((logical_id + 1) % direct_run_len == 0))
        )

        next_id_instrs = 0 if not use_indirect else len(self.mov_imm64_asm("x0", logical_id + 1))
        tail_instrs = 1 if is_last else ((next_id_instrs + 1) if use_indirect else 1)

        if tail_instrs > slots_per_block:
            raise ValueError(f"{prefix} block {logical_id} needs {tail_instrs} instructions")
        if 64 > block_align:
            raise ValueError(f"{prefix} block {logical_id} executes 64B but block_align is only {block_align}B")

        max_branch_pairs = max(0, (slots_per_block - tail_instrs) // 2)
        branch_pairs_per_block = max(0, min(branch_pairs_per_block, max_branch_pairs))
        filler_nops = slots_per_block - tail_instrs - branch_pairs_per_block * 2
        asm_lines = [
            f'__attribute__((used, naked, noinline, aligned({block_align})))\n',
            f'static void {prefix}_block_{logical_id}(void) {{\n',
            '    asm volatile(\n',
        ]

        branch_asm = self.branch_pair_fill_asm(branch_pairs_per_block)
        if branch_asm:
            asm_lines.append(branch_asm)
        filler_asm = self.nop_fill_asm(filler_nops)
        if filler_asm:
            asm_lines.append(filler_asm)

        if is_last:
            asm_lines.append('        "ret\\n\\t"\n')
            asm_lines.append('        ::: "x0", "x9", "x16", "x17", "cc", "memory");\n')
        elif use_indirect:
            asm_lines.extend(self.mov_imm64_asm("x0", logical_id + 1))
            asm_lines.append(f'        "b {dispatcher_symbol}\\n\\t"\n')
            asm_lines.append('        ::: "x0", "x9", "x16", "x17", "cc", "memory");\n')
        else:
            asm_lines.append(f'        "b {target_symbol}\\n\\t"\n')
            asm_lines.append('        ::: "x0", "x9", "x16", "x17", "cc", "memory");\n')

        asm_lines.append("}\n\n")
        return "".join(asm_lines)
