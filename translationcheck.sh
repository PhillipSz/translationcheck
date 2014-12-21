#!/bin/bash

# Script to check for Launchpad Translation
# Uncomment/comment which function you would like to use
#
# Todo: - ask user on frist run and then write a .config
# 
# curently only elementary os apps works!

lang="German" # change to your need; e.g.: "French" or "Greek"
openut=1 # set to 1 to open all untranslated apps in a browser, 0 to only show
openns=1 # set to 1 to open all strings that needs review in a browser, 0 to only show

nameselementary=("noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "maya" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")

namesubuntu=("ubuntu-system-settings" "ubuntu-rest-scopes" "music-app" "address-book-app" "webbrowser-app" "gallery-app" "ubuntu-clock-app" "dialer-app" "sudoku-app" "ubuntu-rssreader-app" "ubuntu-calendar-app" "ubuntu-weather-app" "reminders-app" "unity8" "messaging-app" "indicator-network" "unity-scope-click" "camera-app" "unity-scope-mediascanner" "ubuntu-system-settings-online-accounts" "curucu" "mediaplayer-app" "ubuntu-calculator-app" "notes-app" "unity-scope-scopes" "indicator-location" "telephony-service" "indicator-location")

checktranslations(){

echo "$1"
# its not possible to replace a array name with a varibale
#names=("${nameselementary[@]}") # now replace nameselementary with  a $1
#names="${!1}" 
#names=("${!1[@]}")
#echo ${!1[@]}

if (( "$1" == "elementary" )); then

# start script
# arrays starts with 0 
#

namelength="$((${#nameselementary[@]} -1))"

# just to not be influenced by an env var
shown="" 
opened=""

for i in $(seq 0 $namelength); do

	dw="$(wget -q -O- https://translations.launchpad.net/${nameselementary[$i]}/ | grep -A 30 ">$lang" | grep '<span class="sortkey">'| tail -n2)"

	ut="$(echo "$dw" | head -n1 | egrep -o "[0-9]+")" # ut = untranslated

	ns="$(echo "$dw" | tail -n1 | egrep -o "[0-9]+")" # ns = needs review
	
	if [[ "$ut" =~ [0-9]+ && "$ns" =~ [0-9]+ ]]; then 
		
		if (( "$ut" != "0" )); then
			
			echo "${nameselementary[$i]}:"
			shown=1
			echo "$ut untranslated"
		
			if (( "$openut" == "1" )); then 
					
				xdg-open https://translations.launchpad.net/${nameselementary[$i]}/ 2> /dev/null # don't show error
				opened=1			
			fi
			else
				shown=0
			fi
   
		if (( "$ns" != "0" )); then

			if (( "$openns" == "1" )) && (( "$opened" != "1" )); then 
				xdg-open https://translations.launchpad.net/${nameselementary[$i]}/ 2> /dev/null
			fi

			if (( "$shown" == "1" )); then
				echo "$ns new suggestions"
			else
				echo "${nameselementary[$i]}:"
				echo "$ns new suggestions"
			fi
		fi
	
	opened=0
	
	else
		echo "We have a problem!"
		echo "name = ${nameselementary[$i]}; ut = $ut; ns = $ns"
		exit 1
fi
done

else if (()); then

fi

}

checktranslations elementary # choose elementary or ubuntu-touch
