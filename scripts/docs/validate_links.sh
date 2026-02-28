#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

if ! command -v rg >/dev/null 2>&1; then
  echo "error: ripgrep (rg) is required"
  exit 1
fi

failed=0

while IFS= read -r file; do
  while IFS= read -r token; do
    target=$(printf '%s' "$token" | sed -E 's/.*\]\(([^)]+)\).*/\1/')

    case "$target" in
      http*|mailto:*|\#*|tel:*)
        continue
        ;;
    esac

    # Remove optional anchor/query for filesystem existence checks
    target_no_anchor="${target%%#*}"
    target_no_query="${target_no_anchor%%\?*}"

    base_dir=$(dirname "$file")
    resolved="$base_dir/$target_no_query"

    if [ ! -e "$resolved" ]; then
      echo "broken link: $file -> $target"
      failed=1
    fi
  done < <(rg -o '\[[^]]+\]\([^)]*\)' "$file")
done < <(rg --files -g '*.md')

if [ "$failed" -ne 0 ]; then
  exit 1
fi

echo "ok: no broken internal markdown links"
