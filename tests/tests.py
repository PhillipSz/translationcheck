#!/usr/bin/env python3
#
# Just use "python -m unittest discover -v" to see what happens
#

import unittest
# ugly hack to import translationcheck
# from http://stackoverflow.com/questions/4542352/import-from-sibling-directory
import os
import inspect
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import translationcheck

class getappsTestCase(unittest.TestCase):
    '''Tests for getapps.'''

    def test_get_apps(self):
        '''Test the function to parse the apps to check'''

        self.results = {'elementary': {}, 'ubuntu': {}, 'unityscopes': {}}
        self.results = translationcheck.getapps(self.results)
        self.results_wanted = {'ubuntu': {'ubuntu-terminal-app': [], 'unity-scope-scopes': [], 'ubuntu-rssreader-app': [], 'webbrowser-app': [], 'unity8': [], 'messaging-app': [], 'reminders-app': [], 'ubuntu-keyboard': [], 'help-app': [], 'indicator-location': [], 'dialer-app': [], 'camera-app': [], 'ubuntu-clock-app': [], 'ubuntu-weather-app': [], 'software-center-agent': [], 'today-scope': [], 'twitter-scope': [], 'music-app': [], 'indicator-bluetooth': [], 'ciborium': [], 'ubuntu-rest-scopes': [], 'ubuntu-docviewer-app': [], 'telegram-app': [], 'telephony-service': [], 'address-book-app': [], 'location-service': [], 'ubuntu-calendar-app': [], 'ubuntu-filemanager-app': [], 'unity-scope-mediascanner': [], 'mediaplayer-app': [], 'indicator-network': [], 'sudoku-app': [], 'notes-app': [], 'gallery-app': [], 'ubuntu-system-settings-online-accounts': [], 'ubuntu-ui-toolkit': [], 'ubuntu-calculator-app': []}, 'elementary': {'pantheon-mail': [], 'switchboard-plug-keyboard': [], 'switchboard-plug-locale': [], 'switchboard-plug-onlineaccounts': [], 'wingpanel-indicator-datetime': [], 'switchboard-plug-power': [], 'granite': [], 'appcenter': [], 'switchboard-plug-useraccounts': [], 'gala': [], 'switchboard-plug-about': [], 'switchboard-plug-networking': [], 'wingpanel-indicator-notifications': [], 'switchboard-plug-applications': [], 'wingpanel-indicator-power': [], 'switchboard-plug-a11y': [], 'audience': [], 'wingpanel-indicator-network': [], 'pantheon-calculator': [], 'snap-elementary': [], 'midori': [], 'switchboard-plug-mouse-touchpad': [], 'screenshot-tool': [], 'wingpanel-indicator-bluetooth': [], 'switchboard-plug-parental-controls': [], 'switchboard-plug-sharing': [], 'wingpanel-indicator-sound': [], 'wingpanel-indicator-session': [], 'switchboard-plug-pantheon-shell': [], 'pantheon-photos': [], 'pantheon-greeter': [], 'wingpanel': [], 'scratch': [], 'maya': [], 'elementaryos': [], 'capnet-assist': [], 'switchboard-plug-datetime': [], 'plank': [], 'switchboard-plug-notifications': [], 'switchboard-plug-security-privacy': [], 'wingpanel-indicator-keyboard': [], 'switchboard-plug-display': [], 'slingshot': [], 'pantheon-terminal': [], 'pantheon-files': [], 'switchboard': [], 'noise': [], 'switchboard-plug-printers': []}, 'unityscopes': {'unity-scope-audacious': [], 'unity-scope-yelp': [], 'unity-scope-virtualbox': [], 'unity-scope-etsy': [], 'unity-scope-sshsearch': [], 'unity-scope-stackexchange': [], 'unity-scope-ebay': [], 'unity-scope-pubmed': [], 'unity-scope-firefoxbookmarks': [], 'unity-scope-medicines': [], 'unity-scope-wikipedia': [], 'unity-scope-nullege': [], 'unity-scope-zeitgeistwebhistory': [], 'unity-scope-chromiumbookmarks': [], 'unity-scope-songsterr': [], 'unity-scope-jstor': [], 'unity-scope-clementine': [], 'unity-scope-mediascanner': [], 'unity-scope-deviantart': [], 'unity-scope-isgd': [], 'unity-scope-ubuntushop': [], 'unity-scope-zotero': [], 'unity-scope-calculator': [], 'unity-scope-tomboy': [], 'unity-scope-europeana': [], 'unity-scope-remmina': [], 'unity-scope-yelpplaces': [], 'unity-scope-musique': [], 'unity-scope-gmusicbrowser': [], 'unity-scope-github': [], 'unity-scope-tumblr': [], 'unity-scope-guayadeque': [], 'unity-scope-soundcloud': [], 'unity-scope-manpages': [], 'unity-scope-evolution': [], 'unity-scope-texdoc': [], 'unity-scope-yahoostock': [], 'unity-scope-googlescholar': [], 'unity-scope-askubuntu': [], 'unity-scope-sciencedirect': [], 'unity-scope-gallica': [], 'unity-scope-foursquare': [], 'unity-scope-calibre': [], 'unity-scope-devhelp': [], 'unity-scope-pypi': [], 'unity-scope-recipepuppy': [], 'unity-scope-launchpad': [], 'unity-scope-scopes': [], 'unity-scope-googlenews': [], 'unity-scope-dribbble': [], 'unity-scope-grooveshark': [], 'unity-scope-click': [], 'unity-scope-songkick': [], 'unity-scope-openclipart': [], 'unity-scope-gourmet': [], 'unity-scope-imdb': [], 'unity-scope-wikispecies': [], 'unity-scope-openweathermap': [], 'unity-scope-phpdoc': [], 'unity-scope-googlebooks': [], 'unity-scope-reddit': [], 'unity-scope-colourlovers': []}}
        self.assertEqual(self.results, self.results_wanted)

class getresultsTestCase(unittest.TestCase):
    '''Tests for getresults.
       I just choose these at random and with the hope that they don't change that much.'''

    def test_getresults_elementary(self):
        '''Test the function to parse the webpages for elementary'''

        self.results_e_de = translationcheck.getresults("pantheon-calculator", "German")
        self.assertEqual(self.results_e_de, ('0', '0'))
        self.results_e_de_error = translationcheck.getresults("this-is-not-an-app-:)", "German")
        self.assertEqual(self.results_e_de_error, ('error', 'error'))
        self.results_e_nor = translationcheck.getresults("pantheon-calculator", "Norwegian Bokmal")
        self.assertEqual(self.results_e_nor, ('0', '0'))
        self.results_e_ch = translationcheck.getresults("pantheon-calculator", "Chinese (Simplified)")
        self.assertEqual(self.results_e_ch, ('0', '0'))

    def test_getresults_unityscopes(self):
        '''Test the function to parse the webpages for unity-scopes'''

        self.results_us_de = translationcheck.getresults("unity-scope-remmina", "German")
        self.assertEqual(self.results_us_de, ('0', '0'))
        self.results_us_ch = translationcheck.getresults("unity-scope-remmina", "Chinese (Simplified)")
        self.assertEqual(self.results_us_ch, ('lnf', 'lnf'))

    def test_getresults_ubuntu(self):
        '''Test the function to parse the webpages for ubuntu'''

        self.results_u_de = translationcheck.getresults("ubuntu-keyboard", "German")
        self.assertEqual(self.results_u_de, ('0', '0'))
        self.results_u_uk = translationcheck.getresults("ubuntu-keyboard", "English (United Kingdom)")
        self.assertEqual(self.results_u_uk, ('0', '0'))

if __name__ == '__main__':
    unittest.main()
