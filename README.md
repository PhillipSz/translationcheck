translationcheck for Launchpad
==============================
[![Build Status](https://travis-ci.org/PhillipSz/translationcheck.png)](https://travis-ci.org/PhillipSz/translationcheck)

Just run

	git clone https://github.com/PhillipSz/translationcheck && cd translationcheck

and then

	bash translationcheck.bash -h

to see all options.

Examples:

	bash translationcheck.bash -uel French

	bash translationcheck.bash -el "English (United Kingdom)"

	bash translationcheck.bash -u

(Note: Currently German is the default language! You can change this in line 12 in translationcheck.bash)

To updates this script just run:

	git pull -r

This script requires (normally all should be installed): bash, wget, sed, sort, grep, tput, xdg-open
-------------------------------------------------------------------------------------------------------------------------

Report bugs to https://github.com/PhillipSz/translationcheck/issues
