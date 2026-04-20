#!/usr/bin/env python3

if __package__ in (None, ""):
    from single_common import run_modules
else:
    from .single_common import run_modules


def main():
    run_modules(["data_pointer_chase"])


if __name__ == "__main__":
    main()
