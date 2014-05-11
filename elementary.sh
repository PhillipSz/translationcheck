#!/bin/bash

# Script to check for Launchpad Translation in German 

#To do: 
#https://translations.launchpad.net/ubuntu-system-settings/trunk > Done
#https://translations.launchpad.net/ubuntu-ui-toolkit > Done

#elementary os and Mint and Ubuntu(-Touch)

echo 'Transaltion for Ubuntu in German:'
wget -q -O- https://translations.launchpad.net/ubuntu/trusty | grep -A 32 '>German' | grep sortkey |tail -n1 |cut -c 33- |cut -f1
echo ""

echo 'Unity:'
echo ""

echo 'Unity 8.0:'
wget -q -O- https://translations.launchpad.net/unity8 | grep -A 12 German | grep Translated: |cut -c13-31
echo ""

echo 'Unity phablet:'
wget -q -O- https://translations.launchpad.net/unity/phablet/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo ""

echo 'Transaltion for Linux Mint in German:'
wget -q -O- https://translations.launchpad.net/linuxmint/ | grep -A 12 '>German' | grep Translated: |cut -c13-31
echo ""

echo 'Tralations for elementary os in German:'
echo '
switchboard-plug-default-applications:'
wget -q -O- https://translations.launchpad.net/switchboard-plug-default-applications/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Granite:'
wget -q -O- https://translations.launchpad.net/granite/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Euclide:'
wget -q -O- https://translations.launchpad.net/euclide/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Wingpanel:'
wget -q -O- https://translations.launchpad.net/wingpanel/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Switchboard Plug Keyboard:'
wget -q -O- https://translations.launchpad.net/switchboard-plug-keyboard/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
elementary OS:'
wget -q -O- https://translations.launchpad.net/elementaryos/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Snap:'
wget -q -O- https://translations.launchpad.net/snap-elementary/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Dexter Contacts:'
wget -q -O- https://translations.launchpad.net/dexter-contacts/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Switchboard:'
wget -q -O- https://translations.launchpad.net/switchboard/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Switchboard Plug Power:'
wget -q -O- https://translations.launchpad.net/switchboard-plug-power/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Pantheon Terminal:'
wget -q -O- https://translations.launchpad.net/pantheon-terminal/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Noise:'
wget -q -O- https://translations.launchpad.net/noise/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Maya:'
wget -q -O- https://translations.launchpad.net/maya/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Slingshot:'
wget -q -O- https://translations.launchpad.net/slingshot/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Pantheon Login Screen:'
wget -q -O- https://translations.launchpad.net/pantheon-greeter/+translations | grep -A 12 German | grep Translated: |cut -c13-31

#echo '
#Contractor:'
#wget -q -O- https://translations.launchpad.net/contractor/+translations | grep -A 12 German | grep Translated: |cut -c13-31

echo '
Pantheon Library:'
wget -q -O- https://translations.launchpad.net/libpantheon/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Switchboard Plug Pantheon Shell:'
wget -q -O- https://translations.launchpad.net/switchboard-plug-pantheon-shell/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Scratch:'
wget -q -O- https://translations.launchpad.net/scratch/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Switchboard Plug About:'
wget -q -O- https://translations.launchpad.net/switchboard-plug-about/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Files:'
wget -q -O- https://translations.launchpad.net/pantheon-files/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Midori:'
wget -q -O- https://translations.launchpad.net/midori/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo ''

echo 'Tralations for Ubuntu-Touch in German:'
echo ''

echo 'Ubuntu Touch Developer Preview:'
echo ''

echo '
online-accounts (https://translations.launchpad.net/ubuntu-system-settings-online-accounts/+translations):'
wget -q -O- https://translations.launchpad.net/ubuntu-system-settings-online-accounts/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ui-toolkit (https://translations.launchpad.net/ubuntu-ui-toolkit/+translations):'
wget -q -O- https://translations.launchpad.net/ubuntu-ui-toolkit/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
system-settings (https://translations.launchpad.net/ubuntu-system-settings/+translations):'
wget -q -O- https://translations.launchpad.net/ubuntu-system-settings/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
Click Update Manager (https://translations.launchpad.net/click-update-manager):'
wget -q -O- https://translations.launchpad.net/ubuntu-system-settings/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
messaging:'
wget -q -O- https://translations.launchpad.net/messaging-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
share:'
wget -q -O- https://translations.launchpad.net/share-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
mediaplayer:'
wget -q -O- https://translations.launchpad.net/mediaplayer-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
camera:'
wget -q -O- https://translations.launchpad.net/camera-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
webbrowser:'
wget -q -O- https://translations.launchpad.net/webbrowser-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
gallery:'
wget -q -O- https://translations.launchpad.net/gallery-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
phone:'
wget -q -O- https://translations.launchpad.net/phone-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
dialer:'
wget -q -O- https://translations.launchpad.net/dialer-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
notes:'
wget -q -O- https://translations.launchpad.net/notes-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31

echo ""
echo 'Ubuntu Touch Core Apps:'
echo ""

echo '
ubuntu-weather:'
wget -q -O- https://translations.launchpad.net/ubuntu-weather-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-clock:'
wget -q -O- https://translations.launchpad.net/ubuntu-clock-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-rssreader:'
wget -q -O- https://translations.launchpad.net/ubuntu-rssreader-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-filemanager:'
wget -q -O- https://translations.launchpad.net/ubuntu-filemanager-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
sudoku:'
wget -q -O- https://translations.launchpad.net/sudoku-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-calendar:'
wget -q -O- https://translations.launchpad.net/ubuntu-calendar-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-reminders:'
wget -q -O- https://launchpad.net/reminders-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-music:'
wget -q -O- https://launchpad.net/music-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31
echo '
ubuntu-calculator:'
wget -q -O- https://launchpad.net/ubuntu-calculator-app/+translations | grep -A 12 German | grep Translated: |cut -c13-31

# If you exit the script before it is finished.

#rm wget-log*
