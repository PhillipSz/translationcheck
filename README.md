translationcheck for Launchpad
==============================
[![Build Status](https://travis-ci.org/PhillipSz/translationcheck.png)](https://travis-ci.org/PhillipSz/translationcheck)

Just run

	sudo pip install requests

	git clone https://github.com/PhillipSz/translationcheck && cd translationcheck

and then

	python3 translationcheck.py -h

to see all options.

Examples:

	python3 translationcheck.py -uesl French

	python3 translationcheck.py -el "English (United Kingdom)"

	python3 translationcheck.py -u

	python3 translationcheck.py --update

To updates this script just run:

	git pull -r

(Note: Currently German is the default language! You can change this in line 26 in translationcheck.py)

There is also a bash script which does the same thing, and has mostly the same short options.

-------------------------------------------------------------------------------------------------------------------------

Report bugs to https://github.com/PhillipSz/translationcheck/issues
