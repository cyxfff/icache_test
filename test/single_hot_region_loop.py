#!/usr/bin/env python3

if __package__ in (None, ""):
    from single_common import run_modules
else:
    from .single_common import run_modules


def main():
    run_modules(["hot_region_loop"])


if __name__ == "__main__":
    main()

