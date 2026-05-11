# test Folder Review

## Current State

`test/` currently contains both:

- reusable execution framework (`runner.py`, `csv_layout.py`, `single_common.py`)
- scenario definitions (`experiment_config.py`, `single.py`)
- ad-hoc debugging tools (`combo_debug_tool.py`, `issue_cases/*`)

This is workable, but naming is ambiguous because `test/` is no longer only "tests"; it is also an experiment pipeline.

## Suggested Rename Plan

Do not rename immediately in one shot, because imports currently depend on `test.*` across the repo.

Recommended staged plan:

1. Create a new package `experiments/` and move framework files first:
   - `test/runner.py` -> `experiments/runner.py`
   - `test/csv_layout.py` -> `experiments/csv_layout.py`
2. Move suite definitions:
   - `test/experiment_config.py` -> `experiments/experiment_config.py`
   - `test/single.py` -> `experiments/single.py`
3. Keep debugging scripts together under:
   - `experiments/issue_cases/`
4. Add compatibility shims in `test/` for one transition cycle, then remove `test/`.

## Why This Is Safer

- avoids breaking current import paths in one commit
- keeps runnable scripts stable while refactoring
- makes folder semantics clearer: `experiments/` over `test/`
