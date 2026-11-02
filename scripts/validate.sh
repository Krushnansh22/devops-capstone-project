#!/usr/bin/env bash
#
# validate.sh - check the capstone project against the lab requirements.
#
# Usage:
#   bash scripts/validate.sh
#
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

pass=0
fail=0

ok()  { printf 'PASS  %s\n' "$1"; pass=$((pass + 1)); }
bad() { printf 'FAIL  %s\n      %s\n' "$1" "${2:-}"; fail=$((fail + 1)); }

has() {
    local name="$1" file="$2" needle="$3"
    if [ -f "$file" ] && grep -qF -- "$needle" "$file"; then
        ok "$name"
    else
        bad "$name" "missing '$needle' in $file"
    fi
}

if [ -x "$ROOT/../.venv/bin/python" ]; then
    PYTHON="$ROOT/../.venv/bin/python"
else
    PYTHON="$(command -v python3)"
fi

# ---------------------------------------------------------------------------
# Repository layout
# ---------------------------------------------------------------------------
for f in \
    README.md LICENSE Makefile Procfile requirements.txt setup.cfg .flaskenv \
    Dockerfile wsgi.py bin/entrypoint.sh \
    service/__init__.py service/config.py service/models.py service/routes.py \
    service/common/status.py service/common/error_handlers.py \
    service/common/log_handlers.py service/common/cli_commands.py \
    tests/test_models.py tests/test_routes.py tests/test_cli_commands.py \
    .github/workflows/ci-build.yaml \
    .github/ISSUE_TEMPLATE/story_template.md \
    deploy/deployment.yaml deploy/service.yaml deploy/route.yaml deploy/postgresql.yaml \
    tekton/tasks.yaml tekton/pipeline.yaml tekton/pvc.yaml tekton/pipelinerun.yaml
do
    if [ -f "$f" ]; then ok "file exists: $f"; else bad "file exists: $f" "not found"; fi
done

# ---------------------------------------------------------------------------
# REST API surface
# ---------------------------------------------------------------------------
has "route: health"        service/routes.py 'def health()'
has "route: index"         service/routes.py 'def index()'
has "route: create"        service/routes.py 'def create_accounts()'
has "route: list"          service/routes.py 'def list_accounts()'
has "route: read"          service/routes.py 'def get_accounts(account_id)'
has "route: update"        service/routes.py 'def update_accounts(account_id)'
has "route: delete"        service/routes.py 'def delete_accounts(account_id)'
has "route: POST /accounts"   service/routes.py '@app.route("/accounts", methods=["POST"])'
has "route: GET /accounts"    service/routes.py '@app.route("/accounts", methods=["GET"])'
has "route: PUT /accounts"    service/routes.py 'methods=["PUT"]'
has "route: DELETE /accounts" service/routes.py 'methods=["DELETE"]'
has "model: Account"       service/models.py 'class Account('
has "model: serialize"     service/models.py 'def serialize(self)'
has "model: deserialize"   service/models.py 'def deserialize(self, data)'
has "model: find"          service/models.py 'def find(cls, by_id)'
has "model: find_by_name"  service/models.py 'def find_by_name(cls, name)'

# ---------------------------------------------------------------------------
# Security story
# ---------------------------------------------------------------------------
has "security: Talisman"   service/__init__.py 'Talisman('
has "security: CORS"       service/__init__.py 'CORS('
has "security: CSP"        service/__init__.py 'content_security_policy'

# ---------------------------------------------------------------------------
# CI, container, Kubernetes, Tekton
# ---------------------------------------------------------------------------
has "CI: pytest"           .github/workflows/ci-build.yaml 'pytest'
has "CI: flake8"           .github/workflows/ci-build.yaml 'flake8'
has "CI: postgres service" .github/workflows/ci-build.yaml 'postgres:'
has "Docker: non-root"     Dockerfile 'USER app'
has "Docker: healthcheck"  Dockerfile 'HEALTHCHECK'
has "Docker: entrypoint"   Dockerfile '/app/bin/entrypoint.sh'
has "Docker: gunicorn"     bin/entrypoint.sh 'gunicorn'
has "K8s: probes"          deploy/deployment.yaml 'readinessProbe'
has "K8s: resources"       deploy/deployment.yaml 'resources:'
has "Tekton: cleanup"      tekton/tasks.yaml 'name: cleanup'
has "Tekton: git-clone"    tekton/tasks.yaml 'name: git-clone'
has "Tekton: buildah"      tekton/tasks.yaml 'name: buildah'
has "Tekton: pipeline"     tekton/pipeline.yaml 'name: cd-pipeline'
has "Tekton: deploy step"  tekton/pipeline.yaml 'name: deploy'

# ---------------------------------------------------------------------------
# Documentation and evidence
# ---------------------------------------------------------------------------
has "README: project name" README.md 'devops-capstone-project'
has "README: badge"        README.md 'actions/workflows/ci-build.yaml/badge.svg'
has "story template: As a" .github/ISSUE_TEMPLATE/story_template.md '**As a**'
has "story template: gherkin" .github/ISSUE_TEMPLATE/story_template.md '```gherkin'
has "user stories: 9"      docs/user-stories.md 'Story 9'
has "kanban: closed"       docs/kanban-board.md 'Closed'

for f in \
    evidence/test-results.txt \
    evidence/rest-create.txt \
    evidence/rest-list.txt \
    evidence/rest-read.txt \
    evidence/rest-update.txt \
    evidence/rest-delete.txt \
    evidence/security-headers.txt
do
    if [ -f "$f" ]; then ok "evidence exists: $f"; else bad "evidence exists: $f" "run scripts/capture-evidence.sh"; fi
done

has "evidence: create 201"  evidence/rest-create.txt '201 CREATED'
has "evidence: list 200"    evidence/rest-list.txt '200 OK'
has "evidence: read 200"    evidence/rest-read.txt '200 OK'
has "evidence: update 200"  evidence/rest-update.txt '555-1111'
has "evidence: delete 204"  evidence/rest-delete.txt '204 NO CONTENT'
has "evidence: security"    evidence/security-headers.txt 'X-Content-Type-Options: nosniff'
has "evidence: CORS"        evidence/security-headers.txt 'Access-Control-Allow-Origin: *'

# ---------------------------------------------------------------------------
# YAML syntax
# ---------------------------------------------------------------------------
if "$PYTHON" -c 'import yaml' 2>/dev/null; then
    while IFS= read -r f; do
        if "$PYTHON" -c 'import sys,yaml; list(yaml.safe_load_all(open(sys.argv[1])))' "$f" 2>/dev/null; then
            ok "yaml: $f"
        else
            bad "yaml: $f" "invalid YAML"
        fi
    done < <(find .github deploy tekton -type f \( -name '*.yaml' -o -name '*.yml' \) | sort)
else
    bad "yaml parser" "PyYAML is not installed"
fi

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
if "$PYTHON" -m pytest -q >/tmp/capstone-tests.log 2>&1; then
    ok "unit tests"
else
    bad "unit tests" "see /tmp/capstone-tests.log"
fi

if "$PYTHON" -m flake8 service tests --count --max-line-length=127 >/tmp/capstone-flake8.log 2>&1; then
    ok "flake8"
else
    bad "flake8" "see /tmp/capstone-flake8.log"
fi

printf '\n%d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
