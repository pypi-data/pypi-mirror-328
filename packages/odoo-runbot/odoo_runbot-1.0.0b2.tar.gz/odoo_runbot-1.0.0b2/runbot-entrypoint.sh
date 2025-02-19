#!/usr/bin/env bash

cd $CI_PROJECT_DIR
export CI_JOB_ID=$RANDOM
$CI_PROJECT_DIR/tests/odoo_project/rm-result.sh

set -e
set -x

echo "before_script"
pip install $CI_PROJECT_DIR
cd $CI_PROJECT_DIR/tests/odoo_project
mangono-runbot --verbose diag
mangono-runbot --verbose  init

echo "script"
mangono-runbot --verbose  run
