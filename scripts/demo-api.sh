#!/usr/bin/env bash
#
# demo-api.sh - exercise every REST endpoint and save the output.
#
# Produces:
#   evidence/rest-create.txt
#   evidence/rest-list.txt
#   evidence/rest-read.txt
#   evidence/rest-update.txt
#   evidence/rest-delete.txt
#   evidence/security-headers.txt
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PORT="${PORT:-5000}"
BASE="http://127.0.0.1:$PORT"
DB="$(mktemp -u /tmp/accounts-demo-XXXXXX.db)"
mkdir -p evidence

if [ -x "$ROOT/../.venv/bin/python" ]; then
    PYTHON="$ROOT/../.venv/bin/python"
elif [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
else
    PYTHON="$(command -v python3)"
fi

cleanup() {
    if [ -n "${SERVER_PID:-}" ] && kill -0 "$SERVER_PID" 2>/dev/null; then
        kill "$SERVER_PID" 2>/dev/null || true
        wait "$SERVER_PID" 2>/dev/null || true
    fi
    rm -f "$DB"
}
trap cleanup EXIT

echo "Starting the service on $BASE with database $DB"
FLASK_APP=service:app \
DATABASE_URI="sqlite:///$DB" \
SECRET_KEY="demo-secret" \
"$PYTHON" -m flask run --host 127.0.0.1 --port "$PORT" \
    >/tmp/accounts-demo-server.log 2>&1 &
SERVER_PID=$!

# Wait for the service to become healthy
for _ in $(seq 1 40); do
    if curl -fsS "$BASE/health" >/dev/null 2>&1; then
        break
    fi
    sleep 0.25
done

if ! curl -fsS "$BASE/health" >/dev/null 2>&1; then
    echo "Service failed to start. Log:" >&2
    cat /tmp/accounts-demo-server.log >&2
    exit 1
fi

run() {
    local outfile="$1" cmd="$2"
    {
        echo "\$ $cmd"
        eval "$cmd" 2>&1
        echo
    } > "evidence/$outfile"
}

run rest-create.txt "curl -i -s -X POST $BASE/accounts \
    -H 'Content-Type: application/json' \
    -d '{\"name\":\"John Doe\",\"email\":\"john@doe.com\",\"address\":\"123 Main St.\",\"phone_number\":\"555-1212\"}'"

run rest-list.txt "curl -i -s -X GET $BASE/accounts"

run rest-read.txt "curl -i -s -X GET $BASE/accounts/1"

run rest-update.txt "curl -i -s -X PUT $BASE/accounts/1 \
    -H 'Content-Type: application/json' \
    -d '{\"name\":\"John Doe\",\"email\":\"john@doe.com\",\"address\":\"123 Main St.\",\"phone_number\":\"555-1111\"}'"

run rest-delete.txt "curl -i -s -X DELETE $BASE/accounts/1"

run security-headers.txt "curl -i -s -X GET $BASE/health"

echo "Evidence written to evidence/:"
ls -1 evidence/rest-*.txt evidence/security-headers.txt
