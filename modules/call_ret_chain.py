from typing import Optional


class CallRetChainBuilder:
    @staticmethod
    def normalize_lines_per_func(lines_per_func: int) -> int:
        return max(1, lines_per_func)

    @staticmethod
    def nop_fill_asm(count: int) -> str:
        if count <= 0:
            return ""
        return (
            f'        ".rept {count}\\n\\t"\n'
            '        "nop\\n\\t"\n'
            '        ".endr\\n\\t"\n'
        )

    def emit_function(
        self,
        func_id: int,
        next_func_id: Optional[int],
        lines_per_func: int,
    ) -> str:
        payload_instrs = 2
        tail_instrs = 1 if next_func_id is None else 4
        total_slots = lines_per_func * 16

        if payload_instrs + tail_instrs > total_slots:
            raise ValueError(f"call_ret_func_{func_id} needs {payload_instrs + tail_instrs} instructions")

        filler_nops = total_slots - payload_instrs - tail_instrs
        asm_lines = [
            '__attribute__((used, noinline, naked, aligned(4096)))\n',
            f'static void call_ret_func_{func_id}(void) {{\n',
            '    asm volatile(\n',
            '        "add x9, x9, #1\\n\\t"\n',
            '        "eor x10, x10, x9\\n\\t"\n',
        ]

        filler_asm = self.nop_fill_asm(filler_nops)
        if filler_asm:
            asm_lines.append(filler_asm)

        if next_func_id is not None:
            asm_lines.append('        "str x30, [sp, #-16]!\\n\\t"\n')
            asm_lines.append(f'        "bl call_ret_func_{next_func_id}\\n\\t"\n')
            asm_lines.append('        "ldr x30, [sp], #16\\n\\t"\n')
        asm_lines.append('        "ret\\n\\t"\n')
        asm_lines.append('        ::: "x9", "x10", "x30", "cc", "memory");\n')
        asm_lines.append("}\n\n")
        return "".join(asm_lines)
