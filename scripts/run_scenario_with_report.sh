#!/usr/bin/env bash
# Run scenario tests and print path to latest HTML report.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export QT_QPA_PLATFORM="${QT_QPA_PLATFORM:-offscreen}"

TARGET="${1:-tests/scenario}"
echo "Running scenario tests: $TARGET"
python3 -m pytest "$TARGET" -m scenario -v --tb=short "$@"

LATEST="$(ls -td artifacts/test-reports/*/index.html 2>/dev/null | head -1 || true)"
if [[ -n "$LATEST" ]]; then
  echo ""
  echo "HTML report: file://$ROOT/$LATEST"
  echo "Open: open \"$ROOT/$LATEST\""
else
  echo "No HTML report found under artifacts/test-reports/"
fi
