#!/usr/bin/env python3
"""Entry for make.fun bounty: Sum up 23 November's world news in one image.

Copies the pre-rendered entry image held next to this file to the output
directory (MAKEFUN_OUTPUT_DIR, or /output). Standard library only, no
network, deterministic: the same bytes are written on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
