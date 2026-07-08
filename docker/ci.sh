#!/bin/bash

# CI script
## Tests app

echo "[INFO] Discarding previous containers..."
docker compose -f docker/compose-ci.yaml down --remove-orphans -v
echo "[INFO] Preparing test services..."
docker compose -f docker/compose-ci.yaml up -d
echo "[INFO] CI completed. Discarding containers..."
docker compose -f docker/compose-ci.yaml down --remove-orphans -v
