#!/bin/bash

# Script to check for Launchpad Translation
# Uncomment/comment which function you would like to use
#
# To do: 
# - automaticly open in browser

# curently only elementary os works!

checkelementary(){

lang="German" #change to your need

name=("noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "maya" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")
namelenght="$[${#name[@]}-1]"

for i in `seq 0 $namelenght`
do

	dw="$(wget -q -O- https://translations.launchpad.net/${name[$i]}/ | grep -A 30 ">$lang" | grep '<span class="sortkey">'| tail -n2)"

	#echo "$dw"

	ut="$(echo "$dw" | head -n1 | egrep -o "[0-9]+")"

	ns="$(echo "$dw" | tail -n1 | egrep -o "[0-9]+")"
	
	if [ "$ut" != "0" ]
		then
			echo "${name[$i]}:"
			shown="1"
			echo "$ut untranslated"
		else
			shown="0"
	fi
   
	if [ "$ns" != "0" ]
		then
			if [ "$shown" == "1" ]
				then
					echo "$ns new suggestions"
				else
					echo "${name[$i]}:"
					echo "$ns new suggestions"
			fi
	fi
done
}

checkelementary
