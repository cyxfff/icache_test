#!/usr/bin/env python3

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from test.single_common import run_modules


def main():
    run_modules(["fetch_amplifier"])


if __name__ == "__main__":
    main()
