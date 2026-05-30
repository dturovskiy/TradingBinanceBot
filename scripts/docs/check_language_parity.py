#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

REQUIRED = {
    "overview.md",
    "architecture/project_map.md",
    "research/backtesting.md",
    "testing/testing_guide.md",
    "operations/logging.md",
}

SHARED_REQUIRED = {
    "docs_scope.md",
    "docs_sync_policy.md",
    "style_guide.md",
    "glossary.md",
    "public_sync_manifest.md",
    "public_release_checklist.md",
}

languages = ["en", "ua", "fr"]
missing: list[str] = []

for lang in languages:
    for rel in REQUIRED:
        path = DOCS / lang / rel
        if not path.exists():
            missing.append(f"{lang}: {rel}")

for rel in SHARED_REQUIRED:
    path = DOCS / "shared" / rel
    if not path.exists():
        missing.append(f"shared: {rel}")

if missing:
    print("language parity check failed:")
    for item in sorted(missing):
        print(f"- missing {item}")
    sys.exit(1)

print("ok: language parity satisfied (en/ua/fr + shared docs)")
