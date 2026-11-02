#!/usr/bin/env sh
#
# Container entrypoint.
#
# The service creates its schema at import time. With more than one gunicorn
# worker, every worker would run CREATE TABLE at the same moment and one of
# them loses the race ("table account already exists"). Import the app once
# here, before the workers fork, so the schema exists before they start.
#
set -eu

python -c "import service"

exec gunicorn \
    --bind "0.0.0.0:${PORT:-8080}" \
    --workers "${WEB_CONCURRENCY:-2}" \
    --log-level=info \
    service:app
