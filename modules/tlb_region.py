import random
from typing import Dict, List, Optional, Tuple


class TLBRegionBuilder:
    def shuffled_itlb_phys_order(self, total_funcs: int, seed: int) -> List[int]:
        if total_funcs <= 0:
            return []
        rng = random.Random(seed ^ 0x9E3779B1)
        order = list(range(total_funcs))
        rng.shuffle(order)
        return order

    def constrained_itlb_exec_order(self, phys_order: List[int], seed: int, min_phys_gap: int = 4) -> List[int]:
        if not phys_order:
            return []

        rng = random.Random(seed ^ 0x85EBCA77)
        phys_rank = {func_id: idx for idx, func_id in enumerate(phys_order)}

        remaining = phys_order[:]
        rng.shuffle(remaining)

        order: List[int] = [remaining.pop()]
        while remaining:
            current_func = order[-1]
            current_rank = phys_rank[current_func]

            far = [func_id for func_id in remaining if abs(phys_rank[func_id] - current_rank) >= min_phys_gap]
            mid = [func_id for func_id in remaining if abs(phys_rank[func_id] - current_rank) >= 2]
            pool = far if far else (mid if mid else remaining)

            next_func = rng.choice(pool)
            remaining.remove(next_func)
            order.append(next_func)

        return order

    @staticmethod
    def normalize_lines_per_page(lines_per_page: int) -> int:
        return max(1, lines_per_page)

    @staticmethod
    def normalize_direct_run_len(total_funcs: int, direct_run_len: int) -> int:
        if total_funcs <= 1 or direct_run_len <= 0:
            return 0
        return min(direct_run_len, total_funcs)

    @staticmethod
    def count_indirect_functions(total_funcs: int, mode: str, direct_run_len: int) -> int:
        if mode != "chain" or total_funcs <= 1 or direct_run_len <= 0:
            return 0
        return sum(
            1
            for chain_pos in range(total_funcs - 1)
            if direct_run_len <= 1 or ((chain_pos + 1) % direct_run_len == 0)
        )

    @staticmethod
    def build_chain_maps(
        total_funcs: int,
        exec_order: List[int],
        mode: str,
    ) -> Tuple[Dict[int, Optional[int]], Dict[int, int]]:
        next_map: Dict[int, Optional[int]] = {func_id: None for func_id in range(total_funcs)}
        chain_pos_map: Dict[int, int] = {}

        if mode != "chain":
            return next_map, chain_pos_map

        for pos_idx, func_id in enumerate(exec_order):
            chain_pos_map[func_id] = pos_idx
            next_map[func_id] = exec_order[pos_idx + 1] if pos_idx + 1 < len(exec_order) else None

        return next_map, chain_pos_map

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

    def emit_function(
        self,
        prefix: str,
        func_id: int,
        next_func_id: Optional[int],
        lines_per_page: int,
        mode: str,
        dispatcher_symbol: Optional[str],
        direct_run_len: int,
        chain_pos: Optional[int],
    ) -> str:
        use_indirect = (
            mode == "chain"
            and next_func_id is not None
            and dispatcher_symbol is not None
            and chain_pos is not None
            and direct_run_len > 0
            and (direct_run_len <= 1 or ((chain_pos + 1) % direct_run_len == 0))
        )

        payload_instrs = 2
        next_id_instrs = 0 if not use_indirect else len(self.mov_imm64_asm("x0", next_func_id))
        tail_instrs = 1 if mode != "chain" or next_func_id is None else ((next_id_instrs + 1) if use_indirect else 1)
        total_slots = self.normalize_lines_per_page(lines_per_page) * 16

        if payload_instrs + tail_instrs > total_slots:
            raise ValueError(
                f"itlb/page pool function {func_id} needs {payload_instrs + tail_instrs} instructions"
            )

        filler_nops = total_slots - payload_instrs - tail_instrs

        asm_lines = [
            '__attribute__((used, noinline, naked, aligned(4096)))\n',
            f'static void {prefix}_func_{func_id}(void) {{\n',
            '    asm volatile(\n',
            '        "add x9, x9, #1\\n\\t"\n',
            '        "eor x10, x10, x9\\n\\t"\n',
        ]

        if filler_nops > 0:
            asm_lines.append(
                f'        ".rept {filler_nops}\\n\\t"\n'
                '        "nop\\n\\t"\n'
                '        ".endr\\n\\t"\n'
            )

        if mode == "chain" and next_func_id is not None:
            if use_indirect:
                asm_lines.extend(self.mov_imm64_asm("x0", next_func_id))
                asm_lines.append(f'        "b {dispatcher_symbol}\\n\\t"\n')
                asm_lines.append('        ::: "x0", "x9", "x10", "x16", "x17", "cc", "memory");\n')
            else:
                asm_lines.append(f'        "b {prefix}_func_{next_func_id}\\n\\t"\n')
                asm_lines.append('        ::: "x9", "x10", "cc", "memory");\n')
        else:
            asm_lines.append('        "ret\\n\\t"\n')
            asm_lines.append('        ::: "x9", "x10", "cc", "memory");\n')

        asm_lines.append("}\n\n")
        return "".join(asm_lines)
