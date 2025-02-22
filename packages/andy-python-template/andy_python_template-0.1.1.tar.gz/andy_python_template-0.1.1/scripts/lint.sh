#!/bin/bash
#
# Lint the code base.

echo "Linting Package"
pylint package/

echo "Linting Tests"
pylint tests/