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

def headings(path: Path) -> list[int]:
    return [len(m.group(1)) for line in path.read_text(encoding="utf-8").splitlines()
            if (m := re.match(r"^(#{1,6})\s+", line))]

def links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [m.group(1) for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text)
            if not m.group(1).startswith(("http://","https://","mailto:","tel:","#"))]

errors=[]
for rel in REQUIRED:
    paths=[DOCS/lang/rel for lang in LANGS]
    for p in paths:
        if not p.exists():
            errors.append(f"missing: {p.relative_to(ROOT)}")
    if all(p.exists() for p in paths):
        hs=[headings(p) for p in paths]
        if not (hs[0]==hs[1]==hs[2]):
            errors.append(f"heading hierarchy mismatch: {rel}")
        ls=[links(p) for p in paths]
        if not (ls[0]==ls[1]==ls[2]):
            errors.append(f"cross-language link target mismatch: {rel}")

for path in ROOT.rglob("*.md"):
    for target in links(path):
        clean=target.split("#",1)[0].split("?",1)[0]
        if clean and not (path.parent/clean).exists():
            errors.append(f"broken link: {path.relative_to(ROOT)} -> {target}")

if errors:
    print("language parity validation failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("ok: required paths + heading hierarchy + link targets + internal markdown links")
