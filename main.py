#!/usr/bin/env python3
"""Emit the 25 November 2026 news poster as /output/entry.png.

The poster bytes live in this repository. Prefer the PNG sitting beside
this file; when it is missing, decode the base64 twin instead. Both paths
yield exactly the same bytes, so two runs write identical output. The
program uses no network and reads nothing outside this directory.
"""
import base64, sys
from os import environ
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# The PNG and its base64 twin carry the same poster; the twin is here
# because the GitHub connector only pushes text files, never binaries.
PNG_FILE = ROOT / "entry.png"
B64_FILE = ROOT / "entry.png.b64"


def payload():
    """Poster bytes, from the PNG when present, else its base64 twin."""
    if PNG_FILE.is_file():
        return PNG_FILE.read_bytes()
    return base64.b64decode(B64_FILE.read_bytes())


def run():
    out = Path(environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "entry.png"
    dest.write_bytes(payload())
    dest.chmod(0o644)


if __name__ == "__main__":
    raise SystemExit(run())
