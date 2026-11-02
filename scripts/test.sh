#!/usr/bin/env bash
#
# test.sh - run the unit tests and write the output to evidence/.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ -x "$ROOT/../.venv/bin/python" ]; then
    PYTHON="$ROOT/../.venv/bin/python"
elif [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
else
    PYTHON="$(command -v python3)"
fi

mkdir -p evidence

{
    echo '$ pytest -q'
    "$PYTHON" -m pytest -q 2>&1
} | tee evidence/test-results.txt
