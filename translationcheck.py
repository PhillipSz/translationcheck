#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python source code - replace this with a description of the code and write the code below this text.
"""
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import urllib.request

def translationcheck():
    	
    nameselementary=("pantheon-calculator" "switchboard-plug-datetime" "noise" "switchboard-plug-keyboard" "elementaryos" "snap-elementary" "audience" "slingshot" "switchboard-plug-pantheon-shell" "switchboard-plug-locale" "switchboard-plug-display" "switchboard-plug-applications" "scratch" "gala" "switchboard-plug-about" "pantheon-files" "switchboard-plug-notifications" "switchboard-plug-security-privacy" "switchboard" "wingpanel" "switchboard-plug-power" "appcenter" "pantheon-greeter" "euclide" "switchboard-plug-onlineaccounts" "pantheon-terminal" "granite" "maya" "noise" "pantheon-photos" "midori")

   site=urllib.request.urlopen('https://phillipsz.github.io/about.html')
   b=site.read() 
   print(site) 
translationcheck()
