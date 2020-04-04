#!/usr/bin/env bash

set -e
set -x

pytest --cov=api --cov-report=term-missing api ${@}