#!/bin/sh

# shellcheck source=/dev/null
. /home/pyconarr/.venv/bin/activate
uvicorn pyconarr.main:app
