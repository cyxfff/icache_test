from .block_loop import BlockLoopBuilder


class IndirectTargetSetBuilder(BlockLoopBuilder):
    def emit_target_function(
        self,
        target_id: int,
        total_targets: int,
        block_align: int,
        dispatcher_symbol: str,
    ) -> str:
        is_last = target_id == total_targets - 1
        next_id_instrs = 0 if is_last else len(self.mov_imm64_asm("x0", target_id + 1))
        payload_instrs = 2
        tail_instrs = 1 if is_last else next_id_instrs + 1
        total_slots = 16

        if payload_instrs + tail_instrs > total_slots:
            raise ValueError(f"indirect_target_{target_id} needs {payload_instrs + tail_instrs} instructions")
        if 64 > block_align:
            raise ValueError(f"indirect target block_align must be >= 64, got {block_align}")

        filler_nops = total_slots - payload_instrs - tail_instrs
        asm_lines = [
            f'__attribute__((used, naked, noinline, aligned({block_align})))\n',
            f'static void indirect_target_{target_id}(void) {{\n',
            '    asm volatile(\n',
            '        "add x9, x9, #1\\n\\t"\n',
            '        "eor x10, x10, x9\\n\\t"\n',
        ]

        filler_asm = self.nop_fill_asm(filler_nops)
        if filler_asm:
            asm_lines.append(filler_asm)

        if is_last:
            asm_lines.append('        "ret\\n\\t"\n')
            asm_lines.append('        ::: "x0", "x9", "x10", "x16", "x17", "cc", "memory");\n')
        else:
            asm_lines.extend(self.mov_imm64_asm("x0", target_id + 1))
            asm_lines.append(f'        "b {dispatcher_symbol}\\n\\t"\n')
            asm_lines.append('        ::: "x0", "x9", "x10", "x16", "x17", "cc", "memory");\n')

        asm_lines.append("}\n\n")
        return "".join(asm_lines)
