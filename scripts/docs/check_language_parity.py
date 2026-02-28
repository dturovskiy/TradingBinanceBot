#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

REQUIRED = {
    "overview.md",
    "architecture/project_map.md",
    "testing/testing_guide.md",
    "operations/logging.md",
}

languages = ["en", "ua", "fr"]
missing: list[str] = []

for lang in languages:
    for rel in REQUIRED:
        path = DOCS / lang / rel
        if not path.exists():
            missing.append(f"{lang}: {rel}")

if missing:
    print("language parity check failed:")
    for item in missing:
        print(f"- missing {item}")
    sys.exit(1)

print("ok: language parity satisfied (en/ua/fr)")
