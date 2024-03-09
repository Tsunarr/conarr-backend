#!/bin/sh

# shellcheck source=/dev/null
. /home/pyconarr/.venv/bin/activate
uvicorn --workers 5 --host 0.0.0.0 pyconarr.main:app
