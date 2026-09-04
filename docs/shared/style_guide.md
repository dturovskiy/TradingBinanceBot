# Documentation Style Guide

## Language Rules

- English: technical source language.
- Ukrainian/French: semantically equivalent translations.
- Keep names of code paths and config keys in original form.

## Formatting Rules

- Use short, explicit headings.
- Prefer ordered lists for workflows.
- Use fenced code blocks for commands.
- Use markdown tables only when comparison adds value.

## Path and Command Style

- Wrap file paths in backticks.
- Wrap shell commands in fenced `bash` blocks.
- Keep command examples copy-paste ready.

## Semantic Language Parity

For new or substantively revised multilingual topic pages, use public, non-rendered semantic markers where they improve reviewability:

```text
<!-- parity-key: topic.claim-name -->
```

- Use the same ordered parity-key set in EN, UA, and FR versions of a page.
- A parity key represents a material claim or safety boundary, not a sentence-level translation.
- Keep localized prose natural; do not translate parity-key identifiers.
- The language-parity checker validates required marker sets for topic families that adopt this convention.
- Semantic markers supplement, rather than replace, human review of factual equivalence.

## Change Hygiene

- Avoid stale dates.
- Include absolute date on sync updates.
- Update changelog on every structural or behavioral docs change.
