#!/usr/bin/env bash
#
# publish.sh - create the capstone repository from the IBM template and push.
#
# The lab requires a repository created with "Use this template" (not a fork).
# With GITHUB_TOKEN set, this script creates it through the API. Without a
# token it prints the one-click template URL and waits for you to create it.
#
# Usage:
#   bash scripts/publish.sh [github-username] [repo-name]
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DEFAULT_USER="$(git config user.name 2>/dev/null || true)"
USER="${1:-${GITHUB_USER:-$DEFAULT_USER}}"
REPO="${2:-devops-capstone-project}"
TEMPLATE="ibm-developer-skills-network/aolwx-devops-capstone-template"
TEMPLATE_URL="https://github.com/$TEMPLATE/generate"

if [ -z "$USER" ]; then
    echo "Usage: bash scripts/publish.sh <github-username> [repo-name]" >&2
    exit 2
fi

API="https://api.github.com/repos/$USER/$REPO"
REMOTE="git@github.com:$USER/$REPO.git"

status=$(curl -s -o /dev/null -w '%{http_code}' "$API")

if [ "$status" != "200" ] && [ -n "${GITHUB_TOKEN:-}" ]; then
    echo "Repository not found; creating $USER/$REPO from the template..."
    response=$(curl -s -X POST \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        "https://api.github.com/repos/$TEMPLATE/generate" \
        -d "{\"owner\":\"$USER\",\"name\":\"$REPO\",\"private\":false,\"include_all_branches\":false}")
    echo "$response" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("html_url") or d.get("message"))'
    sleep 3
    status=$(curl -s -o /dev/null -w '%{http_code}' "$API")
fi

if [ "$status" != "200" ]; then
    cat >&2 <<EOF
Repository $USER/$REPO was not found (GitHub API returned $status).

Create it from the IBM template (do NOT fork):

  $TEMPLATE_URL

Use the owner "$USER", the name "$REPO", and choose Public.
Then run this script again.
EOF
    exit 1
fi

echo "Configuring origin -> $REMOTE"
git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE"

echo "Pushing main (replaces the template's initial commit)"
git push -u --force origin main

echo
echo "Repository: https://github.com/$USER/$REPO"
echo "Actions:    https://github.com/$USER/$REPO/actions"
