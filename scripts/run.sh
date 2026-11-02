#!/usr/bin/env bash
#
# run.sh - start the Accounts service locally.
#
# Usage:
#   bash scripts/run.sh [port]
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PORT="${1:-5000}"

# Prefer the shared virtual environment one level up, then a local one.
if [ -x "$ROOT/../.venv/bin/python" ]; then
    PYTHON="$ROOT/../.venv/bin/python"
elif [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
else
    PYTHON="$(command -v python3)"
fi

echo "Starting Accounts service on http://127.0.0.1:$PORT"
echo "Database: ${DATABASE_URI:-sqlite:///accounts.db}"
echo "Press Ctrl+C to stop."

FLASK_APP=service:app \
DATABASE_URI="${DATABASE_URI:-sqlite:///accounts.db}" \
"$PYTHON" -m flask run --host 0.0.0.0 --port "$PORT"
