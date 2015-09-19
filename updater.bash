#!/usr/bin/env bash
#
# updates the apps
#

# old, just to save

checkupdate () {

	update=$(wget -q -O- https://translations.launchpad.net/unity-scopes 2> /dev/null | sed -e 's/(.)+Translatable projects//' -e 's/untranslatable-projects(.)+//' | grep -Eo '<a href="https://launchpad.net/(.)+\+translations"' | sed -e 's/<a href="https:\/\/launchpad.net\///' -e 's/\/+translations"//')
	mapfile -t updatearray < <(echo "$update") # remember mapfile -t lines <file 
	
	#echo "${updatearray[@]}"
	
	declare -n updatearrayold="namesunityscopes"
	
	echo "${updatearray[@]}"
	echo "${updatearrayold[@]}"

	if [[ "${updatearray[@]}" == "${updatearrayold[@]}" ]]; then
		echo "the same, all fine"
	else
		updateready=$(wget -q -O- https://translations.launchpad.net/unity-scopes 2> /dev/null | sed -e 's/(.)+Translatable projects//' -e 's/untranslatable-projects(.)+//' | grep -Eo '<a href="https://launchpad.net/(.)+\+translations"' | sed -e 's/<a href="https:\/\/launchpad.net\///' -e 's/\/+translations"//' -e 's/^/"/' -e 's/$/"/' | tr '\n' ' ' | sed -e 's/^/namesunityscopes=(/' -e 's/ $//' -e 's/$/)/')
		sed "s/namesunityscopes=(.*/$updateready/" translationcheck.bash > translationchecknew.bash
		echo "not the same"
	fi
}


wget -q -O- https://translations.launchpad.net/unity-scopes 2> /dev/null | tr '\n' ' ' | sed -e 's/.*Translatable projects//' -e 's/untranslatable-projects.*//' | tr ' ' '\n' | grep -Eo 'href="https://launchpad.net/(.)+\+translations"' | sed -e 's/href="https:\/\/launchpad.net\///' -e 's/\/+translations"//' > unityscopes

wget -q -O- https://translations.launchpad.net/elementary 2> /dev/null | tr '\n' ' ' | sed -e 's/.*Translatable projects//' -e 's/untranslatable-projects.*//' | tr ' ' '\n' | grep -Eo 'href="https://launchpad.net/(.)+\+translations"' | sed -e 's/href="https:\/\/launchpad.net\///' -e 's/\/+translations"//' > elementary

