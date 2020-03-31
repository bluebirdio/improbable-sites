#!/usr/bin/env bash

PYTHONPATH="$( cd "$(dirname "$0")/../" >/dev/null 2>&1 ; pwd -P )"

set -e
set -x

echo $PYTHONPATH
PYTHONPATH=$PYTHONPATH python api/migrate.py