#!/usr/bin/env bash
#
# test for translationcheck.bash

tests (){
	$HOME/translationcheck/translationcheck.bash -cuesl "german" > /dev/null || echo "error" # it probably never hit this echo
	$HOME/translationcheck/translationcheck.bash -cuesl "french" > /dev/null || echo "error"
	$HOME/translationcheck/translationcheck.bash -cuesl "Chinese (Simplified)" > /dev/null || echo "error"
	$HOME/translationcheck/translationcheck.bash -cuesl "English (United Kingdom)" > /dev/null ||  echo "error"
}


test2 (){
	translationcheck.bash -cuesl "german" > /dev/null || echo "error" # it probably never hit this echo
	translationcheck.bash -cuesl "french" > /dev/null || echo "error"
	translationcheck.bash -cuesl "Chinese (Simplified)" > /dev/null || echo "error"
	translationcheck.bash -cuesl "English (United Kingdom)" > /dev/null ||  echo "error"
}

if [[ -e "$HOME/translationcheck/translationcheck.bash" ]];then
	time tests
elif [[ -e translationcheck.bash ]];then
	time test2
fi

echo $BASH_VERSION

echo "Read the output from the script, as it will always exit with 0!"
