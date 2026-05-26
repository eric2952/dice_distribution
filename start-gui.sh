#!/usr/bin/env bash
set -euo pipefail

xhost +local:docker
cleanup() {
xhost -local:docker
}
trap cleanup EXIT

docker compose up --build "$@"