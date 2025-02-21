#!/usr/bin/env bash

. /opt/kortical-cloud/venvs/app-venv/bin/activate

# Log the installed Python packages
echo "Logging Python package versions..."
pip freeze > /data/pip_freeze.log
cat /data/pip_freeze.log

exec $@