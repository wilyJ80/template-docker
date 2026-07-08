#!/bin/bash

# Dev script
## Prepares dev env

echo "[INFO] Discarding previous containers..."
docker compose --env-file .env -f docker/compose-dev.yaml down --remove-orphans -v
echo "[INFO] Preparing services..."
docker compose --env-file .env -f docker/compose-dev.yaml up -d
echo "[INFO] Services healthy."
