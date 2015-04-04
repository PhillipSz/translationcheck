#!/usr/bin/env bash
#
# test for translationcheck.bash

bash translationcheck.bash -uel "german" > /dev/null || { echo "error" >&2; exit 1; }
echo "works!"
