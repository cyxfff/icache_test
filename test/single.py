#!/usr/bin/env python3

import sys
from pathlib import Path

if __package__ in (None, ""):
    THIS_DIR = Path(__file__).resolve().parent
    if str(THIS_DIR) not in sys.path:
        sys.path.insert(0, str(THIS_DIR))
    from single_common import MODULE_CASE_GROUPS, run_modules
else:
    from .single_common import MODULE_CASE_GROUPS, run_modules


def main():
    run_modules(MODULE_CASE_GROUPS.keys())


if __name__ == "__main__":
    main()
