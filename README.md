translationcheck for Launchpad
==============================
[![Build Status](https://travis-ci.org/PhillipSz/translationcheck.png)](https://travis-ci.org/PhillipSz/translationcheck)

Just run

	sudo pip3 install requests

	git clone https://github.com/PhillipSz/translationcheck && cd translationcheck

and then

	python3 translationcheck.py -h

to see all options.

If you do not specify a language, you will be ask to and then it will be saved in ".conf.ini".

Examples:

	python3 translationcheck.py -uesl French

	python3 translationcheck.py -el "English (United Kingdom)"

	python3 translationcheck.py -u

	python3 translationcheck.py --update

To update this script just run:

	git pull -r

There is also a old bash script which does the same thing, and has mostly the same short options.

-------------------------------------------------------------------------------------------------------------------------

Report bugs to https://github.com/PhillipSz/translationcheck/issues
