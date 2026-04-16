class HotRegionBuilder:
    DEFAULT_BRANCH_PAIRS_PER_UNIT = 3

    @staticmethod
    def emit_hot_unit_body(unit_insns: int = 16, branch_pairs: int = DEFAULT_BRANCH_PAIRS_PER_UNIT) -> str:
        if unit_insns < 2:
            raise ValueError("unit_insns must be >= 2")
        if branch_pairs < 0:
            raise ValueError("branch_pairs must be >= 0")

        max_branch_pairs = (unit_insns - 2) // 2
        branch_pairs = min(branch_pairs, max_branch_pairs)
        filler_nops = unit_insns - 2 - branch_pairs * 2
        out = []
        out.append('        "add x9, x9, #1\\n\\t"\n')
        out.append('        "eor x10, x10, x9\\n\\t"\n')
        # Inject always-not-taken conditional branches to raise br_retired
        # without materially perturbing the hot fetch footprint.
        for label_id in range(1, branch_pairs + 1):
            out.append('        "cmp x9, x9\\n\\t"\n')
            out.append(f'        "b.ne {label_id}f\\n\\t"\n')
            out.append(f'        "{label_id}:\\n\\t"\n')
        if filler_nops > 0:
            out.append(f'        ".rept {filler_nops}\\n\\t"\n')
            out.append('        "nop\\n\\t"\n')
            out.append('        ".endr\\n\\t"\n')
        return "".join(out)

    def emit_region_function(
        self,
        name: str,
        total_bytes: int,
        align: int = 64,
        branch_pairs_per_unit: int = DEFAULT_BRANCH_PAIRS_PER_UNIT,
    ) -> str:
        if total_bytes <= 0:
            return ""

        if total_bytes % 64 != 0:
            raise ValueError(f"{name}: total_bytes must be multiple of 64")
        if total_bytes % 4 != 0:
            raise ValueError(f"{name}: total_bytes must be multiple of 4")

        unit_bytes = 64
        unit_insns = unit_bytes // 4
        unit_count = total_bytes // unit_bytes

        asm_lines = [
            f'__attribute__((used, naked, noinline, aligned({align})))\n',
            f'static void {name}(void) {{\n',
            '    asm volatile(\n',
        ]

        for _ in range(unit_count):
            asm_lines.append(self.emit_hot_unit_body(unit_insns, branch_pairs_per_unit))

        asm_lines.append('        "ret\\n\\t"\n')
        asm_lines.append('        ::: "x9", "x10", "cc", "memory");\n')
        asm_lines.append("}\n\n")
        return "".join(asm_lines)
