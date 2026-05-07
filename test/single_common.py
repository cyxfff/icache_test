#!/usr/bin/env python3

"""Compatibility imports for older scripts.

The single-module runner now lives in test.single so the runnable entry point
and reusable helpers stay in one place.
"""

if __package__ in (None, ""):
    from single import build_row, run_modules
else:
    from .single import build_row, run_modules

__all__ = ["build_row", "run_modules"]
