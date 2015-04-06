#!/usr/bin/env bash
#
# test for translationcheck.bash

bash translationcheck.bash -uel "german" > /dev/null || { echo "error" >&2; exit 1; }
bash translationcheck.bash -uel "french" > /dev/null || { echo "error" >&2; exit 1; }
bash translationcheck.bash -uel "Chinese (Simplified)" > /dev/null || { echo "error" >&2; exit 1; }
bash translationcheck.bash -uel "English (United Kingdom)" > /dev/null || { echo "error" >&2; exit 1; }
echo $BASH_VERSION
echo "works!"
