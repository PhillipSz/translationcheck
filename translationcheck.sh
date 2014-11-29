#!/bin/bash

# Script to check for Launchpad Translation
# Uncomment/comment which function you would like to use
#
# Todo: - check if the input from launchpad really is a number; if not exit 1
# 

# curently only elementary os works!

checkelementary(){

lang="German" # change to your need

openut="0" # set to 1 to open all untranslated apps in a browser, 0 to only show
openns="1" # set to 1 to open all strings that needs review in a browser, 0 to only show

name=("noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "maya" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")
namelenght="$[${#name[@]}-1]"

# just to not be influenced by an env var
shown="" 
opened=""

for i in $(seq 0 $namelenght)
do

	dw="$(wget -q -O- https://translations.launchpad.net/${name[$i]}/ | grep -A 30 ">$lang" | grep '<span class="sortkey">'| tail -n2)"

	ut="$(echo "$dw" | head -n1 | egrep -o "[0-9]+")" # ut = untranslated

	ns="$(echo "$dw" | tail -n1 | egrep -o "[0-9]+")" # ns = needs review
	
	if [ "$ut" != "0" ]
		then
			echo "${name[$i]}:"
			shown="1"
			echo "$ut untranslated"
		
			if [ "$openut" == "1" ]
				then 
					xdg-open https://translations.launchpad.net/${name[$i]}/ 2> /dev/null
					opened="1"			
			fi
		else
			shown="0"
	fi
   
	if [ "$ns" != "0" ]
		then
			if [ "$openns" == "1" ] && [ "$opened" != "1" ]
				then 
					xdg-open https://translations.launchpad.net/${name[$i]}/ 2> /dev/null
			fi

			if [ "$shown" == "1" ]
				then
					echo "$ns new suggestions"
				else
					echo "${name[$i]}:"
					echo "$ns new suggestions"
			fi
	fi
	opened="0"
done
}

checkelementary
