#!/usr/bin/env bash
#
# test for translationcheck.bash

tests (){
	translationcheck.bash -cuesl "german" > /dev/null || echo "error" # it probably never hit this echo
	translationcheck.bash -cuesl "french" > /dev/null || echo "error"
	translationcheck.bash -cuesl "Chinese (Simplified)" > /dev/null || echo "error"
	translationcheck.bash -cuesl "English (United Kingdom)" > /dev/null ||  echo "error"
}

time tests

echo $BASH_VERSION

echo "Read the output from the script, as still script will always exit with 0!"
