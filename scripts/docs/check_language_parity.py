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
    "architecture/module_reference.md",
    "research/backtesting.md",
    "research/evidence_contracts.md",
    "research/microstructure.md",
    "research/options_data.md",
    "research/data_sources.md",
    "testing/testing_guide.md",
    "operations/logging.md",
    "operations/reliability.md",
    "operations/operator_control.md",
)
SEMANTIC_KEY_REQUIRED = {
    "architecture/module_reference.md",
    "research/microstructure.md",
    "research/options_data.md",
    "research/data_sources.md",
    "operations/reliability.md",
    "operations/operator_control.md",
}
SHARED_REQUIRED = (
    "docs_scope.md",
    "docs_sync_policy.md",
    "style_guide.md",
    "glossary.md",
    "public_sync_manifest.md",
    "public_release_checklist.md",
)
PARITY_KEY_RE = re.compile(r"<!--\s*parity-key:\s*([a-z0-9_.-]+)\s*-->")


def headings(path: Path) -> list[int]:
    return [
        len(m.group(1))
        for line in path.read_text(encoding="utf-8").splitlines()
        if (m := re.match(r"^(#{1,6})\s+", line))
    ]


def links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [
        m.group(1)
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text)
        if not m.group(1).startswith(("http://", "https://", "mailto:", "tel:", "#"))
    ]


def parity_keys(path: Path) -> list[str]:
    return PARITY_KEY_RE.findall(path.read_text(encoding="utf-8"))


errors: list[str] = []
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

        key_sets = [parity_keys(path) for path in paths]
        for path, keys in zip(paths, key_sets):
            if len(keys) != len(set(keys)):
                errors.append(f"duplicate semantic parity key: {path.relative_to(ROOT)}")
        if rel in SEMANTIC_KEY_REQUIRED and not all(key_sets):
            errors.append(f"missing semantic parity keys: {rel}")
        if any(key_sets) and not (key_sets[0] == key_sets[1] == key_sets[2]):
            errors.append(f"semantic parity key mismatch: {rel}")

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

print(
    "ok: required language/shared paths + heading hierarchy + link targets + "
    "semantic parity keys + internal markdown links"
)
