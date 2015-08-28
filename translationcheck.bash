#!/usr/bin/env bash
#
# Script to check for Launchpad Translation
#
# curently only elementary os apps, ubuntu-touch apps and uniyt scopes works!
#
# debuging: PS4='+($?) $BASH_SOURCE:$FUNCNAME:$LINENO:'; set -x

clear
shopt -s extglob # we need that later

lang="German" # change this to your needs, e.g.: "French", "Greek", "English (United Kingdom)"

openut="0" # set to 1 to open all untranslated apps in a browser, 0 to only show
openns="0" # set to 1 to open all strings that needs review in a browser, 0 to only show
projects=("unityscopes" "elementary" "ubuntu")

for i in "${projects[@]}"; do
	mapfile -t "$i" <data/"$i"
	#echo "$i:"; declare -n var=$i; echo "${var[@]}"
done

checkupdate () {
	local projects_update=("unityscopes" "elementary") projects_url=("unity-scopes" "elementary") # we can not update ubuntu

	for ((i = 0; i < ${#projects_url[@]}; i++)); do # ${#bla} will give us 2, but an array starts with 0
		local projects_for_file=$(wget -q -O- https://translations.launchpad.net/"${projects_url[$i]}" 2> /dev/null | \
		sed -rn '/Translatable projects/,/untranslatable-projects/ s/.*href="https:\/\/launchpad.net\/(.*)\/\+translations".*/\1/p')

		if [[ "$projects_for_file" =~ ([a-z]|-|[0-9])+ ]]; then 
			echo "$projects_for_file" > data/"${projects_update[$i]}"
		else 
			echo "Ohh something is wrong with "${projects_update[$i]}!" Please report bugs to https://github.com/PhillipSz/translationcheck/issues"
		fi
	done
}

# start script

showhelp(){
echo "Usage: translationcheck [-cueoh] [-l language]"
echo -e "\b"

echo "-u,	check ubuntu apps"
echo "-e,	check elementary apps"
echo "-o,	open all untranslated/needs review apps in a browser"
echo "-c,	checks for new translatable apps from elementary/unity scopes and saves them"
echo "-h,	give this help list"
echo "-l, 	let you specify a language, e.g German, Greek or "English \(United Kingdom\)""
echo "-s,	check unity scopes"

echo -e "\b"
echo "Report bugs to https://github.com/PhillipSz/translationcheck/issues"
}

checktranslations(){

	# I use declare to be able to use a varibale as array name

	declare -n names="$1" # or use typeset, but it's the same in bash; # we need names... as input here

	# How many programms we would like to check? (-1 because array start with 0)
 
	local namelength="$((${#names[@]} -1))"

	#echo "$namelength"

	case "$1" in 
		ubuntu)
			#wget -q -O- https://translations.launchpad.net/ubuntu/X??/ >/dev/null && echo "New version x is now translatable"
			echo "Let's see what we have for ubuntu in $lang:"
			echo -e "\b"
			;;
		elementary)
			echo "Let's see what we have for elementary in $lang:"
			echo -e "\b"
			;;
		unityscopes)
			echo "Let's see what we have for the unity scopes in $lang:"
			echo -e "\b"
			;;
	esac
	
	# just to not be influenced by an env var; ns = needs review; ut = untranslated
	local shown opened textbreak red green dw ns ut red=$(tput setaf 1) green=$(tput setaf 2)

	for ((i = 0; i <= namelength; i++)); do

		parallel (){

			dw="$( wget -q -O- "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null | grep -i -A 30 ">$lang<" | \
			grep '<span class="sortkey">' | tail -n2 )"

			ut="$( echo "$dw" | head -n1 | egrep -o "[0-9]+" )"

			ns="$( echo "$dw" | tail -n1 | egrep -o "[0-9]+" )"

			# lets check if that worked
			[[ "$ut" != *[0-9] || "$ns" != *[0-9] ]] \
			&& echo "input error! Debug: lang = $lang; name = ${names[$i]}; ut = $ut; ns = $ns; \$1 = $1" >&2 && exit 1

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
					echo -e "$green""$ns new suggestion(s)"; tput sgr0
				else
					echo "${names[$i]}:"
					echo -e "$green""$ns new suggestion(s)"; tput sgr0
				fi
			fi

			[[ "$textbreak" == "1" ]] && echo -e "\b"

			# clear vars for new loop round
			unset opened shown textbreak

}

parallel & # if the fuction is done it just throws out the result; this may give us a wrong formated output.
done
wait # we must wait until all parallel's are done; the problem here is that we can not get the exit status of all programms
}

# we can not use a function here

# getopts: no --option
# old style $1 and shift code:  we can add that, but its too long
# we could also use http://mywiki.wooledge.org/BashFAQ/035

while getopts ":cuesol:h" opt; do
	case "$opt" in
	c)
		checkupdate
		;;
	u)
		checktranslations ubuntu
		;;
	e)
		checktranslations elementary
		;;
	s)
		checktranslations unityscopes
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
