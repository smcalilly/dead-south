#!/bin/bash
result=0
trap 'result=1' ERR

flake8 my_new_app tests
npx eslint dead_south/static/js/*.js
pytest -sxv

exit "$result"
