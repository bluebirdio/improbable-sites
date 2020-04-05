#!/usr/bin/env bash

set -e
set -x

pytest --cov=sites --cov=samey --cov-report=term-missing sites ${@}