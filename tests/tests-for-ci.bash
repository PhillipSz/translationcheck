#!/usr/bin/env bash
#
# test for translationcheck.bash

tests (){
	translationcheck.bash -uesl "german" > /dev/null || echo "error" # it probably never hit this echo
	translationcheck.bash -uesl "french" > /dev/null || echo "error"
	translationcheck.bash -uesl "Chinese (Simplified)" > /dev/null || echo "error"
	translationcheck.bash -uesl "English (United Kingdom)" > /dev/null ||  echo "error"
}

time tests

echo $BASH_VERSION

echo "Read the output from the script, as still script will always exit with 0!"
