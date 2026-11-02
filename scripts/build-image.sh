#!/usr/bin/env bash
#
# build-image.sh - build the accounts image and record evidence.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

IMAGE="${IMAGE:-accounts:1}"
mkdir -p evidence

{
    echo "\$ docker build --rm --pull --tag $IMAGE ."
    docker build --rm --pull --tag "$IMAGE" .
    echo
    echo "\$ docker image ls $IMAGE"
    docker image ls "$IMAGE"
} 2>&1 | tee evidence/kube-images.txt
