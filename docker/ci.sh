#!/bin/bash

# CI script
## Tests app

echo "[INFO] Discarding previous containers..."
docker compose -f docker/compose-ci.yaml down --remove-orphans -v

echo "[INFO] Building project..."
docker compose --env-file .env -f docker/compose-ci.yaml build

echo "[INFO] Preparing test services..."
docker compose -f docker/compose-ci.yaml run --rm db_static_checks
docker compose -f docker/compose-ci.yaml up -d db_test_postgresql
docker compose -f docker/compose-ci.yaml run --rm db_tests

echo "[INFO] CI completed. Discarding containers..."
docker compose -f docker/compose-ci.yaml down --remove-orphans -v
