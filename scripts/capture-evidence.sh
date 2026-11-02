#!/usr/bin/env bash
#
# capture-evidence.sh - regenerate every piece of local evidence.
#
# Usage:
#   bash scripts/capture-evidence.sh
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "== Unit tests =="
bash scripts/test.sh

echo
echo "== REST API demo =="
bash scripts/demo-api.sh

echo
echo "== Static analysis =="
if [ -x "$ROOT/../.venv/bin/python" ]; then
    PYTHON="$ROOT/../.venv/bin/python"
else
    PYTHON="$(command -v python3)"
fi
"$PYTHON" -m flake8 service tests --count --max-line-length=127 --statistics \
    > evidence/flake8.txt 2>&1 || true

echo
echo "Evidence files:"
ls -1 evidence/
