#!/bin/bash

# Script to check for Launchpad Translation in German 

#To do: 

#elementary os and Mint and Ubuntu(-Touch)

name=("granite" "maya" "noise" "pantheon-photos" "midori")
namelenght="$[${#name[@]}-1]"

for i in `seq 0 $namelenght`
do

	dw="$(wget -q -O- https://translations.launchpad.net/${name[$i]}/ | grep -A 30 '>German' | grep '<span class="sortkey">'| tail -n2)"

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
			if [ "$shown" == "1"]
				then
					echo "$ns new suggestions"
				else
					echo "${name[$i]}:"
					echo "$ns new suggestions"
			fi
	fi
done
