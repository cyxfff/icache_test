class PltStubChainBuilder:
    @staticmethod
    def emit_payload(filler_nops: int) -> str:
        out = [
            '        "add x9, x9, #1\\n\\t"\n',
            '        "eor x10, x10, x9\\n\\t"\n',
        ]
        if filler_nops > 0:
            out.append(f'        ".rept {filler_nops}\\n\\t"\n')
            out.append('        "nop\\n\\t"\n')
            out.append('        ".endr\\n\\t"\n')
        return "".join(out)

    def emit_caller(self, func_id: int) -> str:
        filler_nops = 8
        return "".join(
            [
                '__attribute__((used, noinline, naked, aligned(4096)))\n',
                f'static void plt_caller_{func_id}(void) {{\n',
                '    asm volatile(\n',
                '        "stp x29, x30, [sp, #-16]!\\n\\t"\n',
                '        "mov x29, sp\\n\\t"\n',
                self.emit_payload(filler_nops),
                f'        "bl plt_stub_{func_id}\\n\\t"\n',
                '        "ldp x29, x30, [sp], #16\\n\\t"\n',
                '        "ret\\n\\t"\n',
                '        ::: "x9", "x10", "x29", "x30", "cc", "memory");\n',
                "}\n\n",
            ]
        )

    def emit_stub(self, func_id: int) -> str:
        return "".join(
            [
                '__attribute__((used, noinline, naked, aligned(4096)))\n',
                f'static void plt_stub_{func_id}(void) {{\n',
                '    asm volatile(\n',
                f'        "b plt_callee_{func_id}\\n\\t"\n',
                '        ::: "cc", "memory");\n',
                "}\n\n",
            ]
        )

    def emit_callee(self, func_id: int) -> str:
        filler_nops = 12
        return "".join(
            [
                '__attribute__((used, noinline, naked, aligned(4096)))\n',
                f'static void plt_callee_{func_id}(void) {{\n',
                '    asm volatile(\n',
                self.emit_payload(filler_nops),
                '        "ret\\n\\t"\n',
                '        ::: "x9", "x10", "cc", "memory");\n',
                "}\n\n",
            ]
        )
