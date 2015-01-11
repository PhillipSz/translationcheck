#!/bin/bash

# Script to check for Launchpad Translation
#
# Todo: - ask user on frist run and then write a .config or use options like ./translationcheck -a -v -f
# 
# curently only elementary os apps and ubuntu-touch apps works!
#

lang="German" # change this to your needs, e.g.: "French" or "Greek"

openut="1" # set to 1 to open all untranslated apps in a browser, 0 to only show
openns="1" # set to 1 to open all strings that needs review in a browser, 0 to only show

checkubuntu="0" # set to 1 to check ubuntu apps, 0 to not do so 
checkelementary="1" # set to 1 to check elementary apps, 0 to not do so

nameselementary=("noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")
namesubuntu=("ubuntu-system-settings" "ubuntu-rest-scopes" "music-app" "address-book-app" "webbrowser-app" "gallery-app" "ubuntu-clock-app" "dialer-app" "sudoku-app" "ubuntu-rssreader-app" "ubuntu-calendar-app" "ubuntu-weather-app" "reminders-app" "unity8" "messaging-app" "indicator-network" "unity-scope-click" "camera-app" "unity-scope-mediascanner" "ubuntu-system-settings-online-accounts" "curucu" "mediaplayer-app" "ubuntu-calculator-app" "notes-app" "unity-scope-scopes" "indicator-location" "telephony-service" "indicator-location")

checktranslations(){

# start script
# I use declare to be able to use a varibale as array name

declare -n names="$1" # or use typeset, but it the same in bash; # we need namesubuntu or nameselementary as input here

# How many programms we would like to check? (-1 because array start with 0)
 
namelength="$((${#names[@]} -1))"

# echo "$namelength"

# just to not be influenced by an env var
shown="" 
opened=""

for i in $(seq 0 $namelength); do

	dw="$(wget -q -O- https://translations.launchpad.net/${names[$i]}/ | grep -A 30 ">$lang" | grep '<span class="sortkey">'| tail -n2)"

	ut="$(echo "$dw" | head -n1 | egrep -o "[0-9]+")" # ut = untranslated

	ns="$(echo "$dw" | tail -n1 | egrep -o "[0-9]+")" # ns = needs review
	
	if [[ "$ut" =~ [0-9]+ && "$ns" =~ [0-9]+ ]]; then # in case $ut or $ns = "" give an error
		
		if [[ "$ut" != "0" ]]; then
			
			echo "${names[$i]}:"
			shown="1"
			echo "$ut untranslated"
		
			if [[ "$openut" == "1" ]]; then 
					
				xdg-open https://translations.launchpad.net/${names[$i]}/ 2> /dev/null
				opened="1"			
			fi
			else
				shown="0"
			fi
   
		if [[ "$ns" != "0" ]]; then

			if [[ "$openns" == "1" && "$opened" != "1" ]]; then 
				xdg-open https://translations.launchpad.net/${names[$i]}/ 2> /dev/null
			fi

			if [[ "$shown" == "1" ]]; then
				echo "$ns new suggestions"
			else
				echo "${names[$i]}:"
				echo "$ns new suggestions"
			fi
		fi
	
	opened="0" # clear vars for new loop round
	shown=""
	
	else
		echo "We have a problem!"
		echo "Debug: name = ${names[$i]}; ut = $ut; ns = $ns; \$1 = $1"
		exit 1
fi
done
}

# Todo: make this part not so static!

if [[ "$checkubuntu" == "1" ]]; then
	checktranslations namesubuntu
fi

if [[ "$checkelementary" == "1" ]]; then
	checktranslations nameselementary
fi
