#!/bin/bash
# scripts/release.sh -- Commands to run on every Heroku release

set -euo pipefail

python manage.py collectstatic --noinput
python manage.py migrate --noinput
