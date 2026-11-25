#!/usr/bin/env python3
"""Write the 25 November 2026 world-news summary image to /output/entry.png.

The image is bundled in this repository. If entry.png sits next to this
program it is copied byte for byte; otherwise the base64 bundle entry.png.b64
is decoded (the GitHub connector only pushes text, so the PNG travels as
base64 — the bytes written are identical either way). Deterministic: two runs
write identical bytes. No network.
"""
import base64
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PNG = os.path.join(HERE, "entry.png")
B64 = os.path.join(HERE, "entry.png.b64")


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if os.path.exists(PNG):
        with open(PNG, "rb") as fsrc, open(dst, "wb") as fdst:
            shutil.copyfileobj(fsrc, fdst, length=1024 * 1024)
    else:
        with open(B64, "rb") as fsrc, open(dst, "wb") as fdst:
            base64.decode(fsrc, fdst)
    os.chmod(dst, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
