#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
LANGS = ("en", "ua", "fr")
REQUIRED = (
    "overview.md",
    "architecture/project_map.md",
    "architecture/execution_recovery.md",
    "research/backtesting.md",
    "research/evidence_contracts.md",
    "testing/testing_guide.md",
    "operations/logging.md",
)
SHARED_REQUIRED = (
    "docs_scope.md",
    "docs_sync_policy.md",
    "style_guide.md",
    "glossary.md",
    "public_sync_manifest.md",
    "public_release_checklist.md",
)

def headings(path: Path) -> list[int]:
    return [len(m.group(1)) for line in path.read_text(encoding="utf-8").splitlines()
            if (m := re.match(r"^(#{1,6})\s+", line))]

def links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [m.group(1) for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text)
            if not m.group(1).startswith(("http://", "https://", "mailto:", "tel:", "#"))]

errors = []
for rel in REQUIRED:
    paths = [DOCS / lang / rel for lang in LANGS]
    for path in paths:
        if not path.exists():
            errors.append(f"missing: {path.relative_to(ROOT)}")
    if all(path.exists() for path in paths):
        heading_sets = [headings(path) for path in paths]
        if not (heading_sets[0] == heading_sets[1] == heading_sets[2]):
            errors.append(f"heading hierarchy mismatch: {rel}")
        link_sets = [links(path) for path in paths]
        if not (link_sets[0] == link_sets[1] == link_sets[2]):
            errors.append(f"cross-language link target mismatch: {rel}")

for rel in SHARED_REQUIRED:
    path = DOCS / "shared" / rel
    if not path.exists():
        errors.append(f"missing shared: {rel}")

for path in ROOT.rglob("*.md"):
    for target in links(path):
        clean = target.split("#", 1)[0].split("?", 1)[0]
        if clean and not (path.parent / clean).exists():
            errors.append(f"broken link: {path.relative_to(ROOT)} -> {target}")

if errors:
    print("language parity validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("ok: required language/shared paths + heading hierarchy + link targets + internal markdown links")
