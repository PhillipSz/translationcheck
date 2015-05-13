#!/usr/bin/env bash
#
# Script to check for Launchpad Translation
#
# TODO: check bugs on githubb
# curently only elementary os apps and ubuntu-touch apps works!
#

shopt -s extglob # we need that later

lang="German" # change this to your needs, e.g.: "French", "Greek", "English (United Kingdom)"

openut="0" # set to 1 to open all untranslated apps in a browser, 0 to only show
openns="0" # set to 1 to open all strings that needs review in a browser, 0 to only show

checkubuntu="0" # set to 1 to check ubuntu apps, 0 to not do so
checkelementary="0" # set to 1 to check elementary apps, 0 to not do so

nameselementary=("pantheon-calculator" "switchboard-plug-datetime" "noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")
namesubuntu=("ubuntu-docviewer-app" "ubuntu-system-settings" "ubuntu-rest-scopes" "music-app" "address-book-app" "webbrowser-app" "gallery-app" "ubuntu-clock-app" "dialer-app" "sudoku-app" "ubuntu-rssreader-app" "ubuntu-calendar-app" "ubuntu-weather-app" "reminders-app" "unity8" "messaging-app" "indicator-network" "unity-scope-click" "camera-app" "unity-scope-mediascanner" "ubuntu-system-settings-online-accounts" "curucu" "mediaplayer-app" "ubuntu-calculator-app" "notes-app" "unity-scope-scopes" "indicator-location" "telephony-service" "indicator-location")

# start script

showhelp(){
echo "Usage: translationcheck [-ueoh] [-l language]"
echo -e "\b"

echo "-u,	check ubuntu apps"
echo "-e,	check ubuntu apps"
echo "-o,	open all untranslated/needs review apps in a browser"
echo "-h,	give this help list"
echo "-l, 	let you specify a language, e.g German, Greek or "English \(United Kingdom\)""

echo -e "\b"
echo "Report bugs to https://github.com/PhillipSz/translationcheck/issues"
}

checktranslations(){

# I use declare to be able to use a varibale as array name

declare -n names="$1" # or use typeset, but it the same in bash; # we need namesubuntu or nameselementary as input here

# How many programms we would like to check? (-1 because array start with 0)
 
local namelength="$((${#names[@]} -1))"

# echo "$namelength"

echo "Let's what we have for $lang:"
echo -e "\b"

# just to not be influenced by an env var
local shown
local opened
local textbreak
local red # declare these here, to be able to check the exit status; when we use var=$(..) # https://github.com/koalaman/shellcheck/wiki/SC2155
local green
local dw
local ns
local ut
red=$(tput setaf 1)
green=$(tput setaf 2)

for ((i = 0; i <= namelength; i++)); do
	dw="$( wget -q -O- "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null | grep -i -A 30 ">$lang<" | grep '<span class="sortkey">' | tail -n2 )"

	ut="$( echo "$dw" | head -n1 | egrep -o "[0-9]+" )" # ut = untranslated

	ns="$( echo "$dw" | tail -n1 | egrep -o "[0-9]+" )" # ns = needs review

	# lets check if that worked
	if [[ "$ut" != *[0-9] || "$ns" != *[0-9] ]]; then
		echo "input error! Debug: lang = $lang; name = ${names[$i]}; ut = $ut; ns = $ns; \$1 = $1" >&2
		exit 1
	fi

	#echo "vars(${names[$i]}): $ut + $ns" # debugging
	
	if [[ "$ut" != "0" ]]; then
		
		textbreak="1"
		echo "${names[$i]}:"
		shown="1"
		echo -e "$red""$ut untranslated"; tput sgr0

		if [[ "$openut" == "1" ]]; then
					
			xdg-open "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null
			opened="1"		
		fi
	else
		shown="0"
	fi
   
	if [[ "$ns" != "0" ]]; then

		textbreak="1"
		if [[ "$openns" == "1" && "$opened" != "1" ]]; then
			xdg-open "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null
		fi

		if [[ "$shown" == "1" ]]; then
			echo -e "$green""$ns new suggestions"; tput sgr0
		else
			echo "${names[$i]}:"
			echo -e "$green""$ns new suggestions"; tput sgr0
		fi
	fi
	
	if [[ "$textbreak" == "1" ]]; then
		echo -e "\b"
	fi

	# clear vars for new loop round
	unset opened
	unset shown
	unset textbreak
done
}

# we can not use a function here

while getopts ":ueovl:h" opt; do
	case "$opt" in
	u)
		checkubuntu="1"
		;;
	e)
		checkelementary="1"
		;;
	o)
		openns="1"
		openut="1"
		;;
	h)
		showhelp
		exit 0
		;;
	l)
		lang="$OPTARG"
		;;
	\?)
		echo "Invalid option (use -h to display the help page): -$OPTARG" >&2
		exit 1
		;;
	:)
		echo "Option -$OPTARG requires an argument" >&2
		exit 1
		;;
	esac
done


# getopts: no --option
# old style $1 and shift code:  we can add that, but its too long
# we could also use http://mywiki.wooledge.org/BashFAQ/035

# TODO: make this part not so static!

if [[ "$checkubuntu" == "1" ]]; then
	wget -q -O- https://translations.launchpad.net/ubuntu/wily/ >/dev/null && echo "New version wily is now translatable on launchpad!!! Update the script"
	checktranslations namesubuntu
fi

if [[ "$checkelementary" == "1" ]]; then
	checktranslations nameselementary
fi
