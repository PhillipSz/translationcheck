#!/usr/bin/env bash
#
# Script to check for Launchpad Translation
#
# curently only elementary os apps, ubuntu-touch apps and unity scopes works!
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
echo "-l, 	let you specify a language, e.g. German, Greek or "English \(United Kingdom\)""
echo "-s,	check unity scopes"

echo -e "\b"
echo "Report bugs to https://github.com/PhillipSz/translationcheck/issues"
}

checktranslations(){

	# I use declare to be able to use a varibale as array name

	declare -n names="$1" # or use typeset, but it's the same in bash; # we need names... as input here

	# How many programms we would like to check? (-1 because array start with 0)
 
	local namelength="$((${#names[@]} -1))"

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
	
	# just to not be influenced by an env var
	local shown opened textbreak results red=$(tput setaf 1) green=$(tput setaf 2) yellow=$(tput setaf 3)

	for ((i = 0; i <= namelength; i++)); do

		parallel (){

			#Check if the start in sed is a good one or can give us errors?
			mapfile -t results < <(wget -q -O- "https://translations.launchpad.net/${names[$i]}/" | grep -iA 30 ">$lang<" | \
			sed -rn '/<img/,$ s/.*<span class="sortkey">(.*)<\/span>/\1/p')

			# lets check if that worked
			# we assume that it has no translations. We may find a better way?
			[[ "${results[0]}" != *[0-9] || "${results[1]}" != *[0-9] ]] \
			&& { echo "${names[$i]}:"; echo "$yellow""This app probably has no translations in $lang yet!"; tput sgr0; \
			echo -e "\b";} >&2 && exit 1
			#&& echo "input error! Debug: lang = $lang; name = ${names[$i]}; results = ${results[@]}" >&2 && exit 1

			if [[ "${results[0]}" != "0" ]]; then

				textbreak="1"
				echo "${names[$i]}:"
				shown="1"
				echo -e "$red""${results[0]} untranslated"; tput sgr0

				if [[ "$openut" == "1" ]]; then

					xdg-open "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null
					opened="1"
				fi
			else
				shown="0"
			fi

			if [[ "${results[1]}" != "0" ]]; then

				textbreak="1"
				if [[ "$openns" == "1" && "$opened" != "1" ]]; then
					xdg-open "https://translations.launchpad.net/${names[$i]}/" 2> /dev/null
				fi

				if [[ "$shown" == "1" ]]; then
					echo -e "$green""${results[1]} new suggestion(s)"; tput sgr0
				else
					echo "${names[$i]}:"
					echo -e "$green""${results[1]} new suggestion(s)"; tput sgr0
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
		checkubuntu="1"
		;;
	e)
		checkelementary="1"
		;;
	s)
		checkunityscopes="1"
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

# We can not directly call these functions in getopts because we need $lang to be set before we run anything else.
[[ "$checkubuntu" == "1" ]] && checktranslations ubuntu
[[ "$checkelementary" == "1" ]] && checktranslations elementary
[[ "$checkunityscopes" == "1" ]] && checktranslations unityscopes
