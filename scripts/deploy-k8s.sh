#!/usr/bin/env bash
#
# deploy-k8s.sh - deploy the service to Kubernetes/OpenShift.
#
# Usage:
#   bash scripts/deploy-k8s.sh
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

mkdir -p evidence

if ! command -v kubectl >/dev/null 2>&1 && ! command -v oc >/dev/null 2>&1; then
    echo "kubectl/oc not found. Run this inside the IBM Cloud IDE or a cluster shell." >&2
    exit 1
fi

CLI="kubectl"
command -v oc >/dev/null 2>&1 && CLI="oc"

echo "Applying manifests with $CLI"
$CLI apply -f deploy/postgresql.yaml
$CLI apply -f deploy/deployment.yaml
$CLI apply -f deploy/service.yaml
$CLI apply -f deploy/route.yaml || echo "Route is OpenShift-only; skipped on plain Kubernetes."

echo "Waiting for the rollout"
$CLI rollout status deployment/accounts --timeout=180s

{
    echo "\$ $CLI get all -l app=accounts"
    $CLI get all -l app=accounts
} | tee evidence/kube-deploy-accounts.txt
