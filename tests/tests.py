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
        self.results_wanted = {'ubuntu': {'telegram-app': [], 'ubuntu-calendar-app': [], 'ubuntu-calculator-app': [], 'ubuntu-keyboard': [], 'music-app': [], 'ubuntu-terminal-app': [], 'indicator-network': [], 'camera-app': [], 'unity-scope-scopes': [], 'ubuntu-rssreader-app': [], 'ubuntu-system-settings-online-accounts': [], 'gallery-app': [], 'reminders-app': [], 'dialer-app': [], 'software-center-agent': [], 'ubuntu-ui-toolkit': [], 'today-scope': [], 'webbrowser-app': [], 'unity-scope-mediascanner': [], 'ubuntu-clock-app': [], 'indicator-bluetooth': [], 'messaging-app': [], 'mediaplayer-app': [], 'telephony-service': [], 'ubuntu-docviewer-app': [], 'indicator-location': [], 'unity8': [], 'ubuntu-rest-scopes': [], 'ciborium': [], 'help-app': [], 'location-service': [], 'ubuntu-filemanager-app': [], 'address-book-app': [], 'ubuntu-weather-app': [], 'sudoku-app': [], 'twitter-scope': [], 'notes-app': []}, 'unityscopes': {'unity-scope-click': [], 'unity-scope-jstor': [], 'unity-scope-ubuntushop': [], 'unity-scope-firefoxbookmarks': [], 'unity-scope-medicines': [], 'unity-scope-sshsearch': [], 'unity-scope-tumblr': [], 'unity-scope-songsterr': [], 'unity-scope-chromiumbookmarks': [], 'unity-scope-wikispecies': [], 'unity-scope-zeitgeistwebhistory': [], 'unity-scope-clementine': [], 'unity-scope-gourmet': [], 'unity-scope-gmusicbrowser': [], 'unity-scope-mediascanner': [], 'unity-scope-etsy': [], 'unity-scope-pypi': [], 'unity-scope-yelp': [], 'unity-scope-soundcloud': [], 'unity-scope-audacious': [], 'unity-scope-askubuntu': [], 'unity-scope-gallica': [], 'unity-scope-deviantart': [], 'unity-scope-wikipedia': [], 'unity-scope-scopes': [], 'unity-scope-manpages': [], 'unity-scope-devhelp': [], 'unity-scope-tomboy': [], 'unity-scope-colourlovers': [], 'unity-scope-guayadeque': [], 'unity-scope-grooveshark': [], 'unity-scope-musique': [], 'unity-scope-calibre': [], 'unity-scope-texdoc': [], 'unity-scope-calculator': [], 'unity-scope-virtualbox': [], 'unity-scope-github': [], 'unity-scope-googlescholar': [], 'unity-scope-dribbble': [], 'unity-scope-openweathermap': [], 'unity-scope-yahoostock': [], 'unity-scope-songkick': [], 'unity-scope-zotero': [], 'unity-scope-stackexchange': [], 'unity-scope-phpdoc': [], 'unity-scope-reddit': [], 'unity-scope-remmina': [], 'unity-scope-foursquare': [], 'unity-scope-imdb': [], 'unity-scope-nullege': [], 'unity-scope-recipepuppy': [], 'unity-scope-evolution': [], 'unity-scope-googlebooks': [], 'unity-scope-pubmed': [], 'unity-scope-ebay': [], 'unity-scope-isgd': [], 'unity-scope-openclipart': [], 'unity-scope-googlenews': [], 'unity-scope-sciencedirect': [], 'unity-scope-yelpplaces': [], 'unity-scope-europeana': [], 'unity-scope-launchpad': []}, 'elementary': {'screenshot-tool': [], 'pantheon-terminal': [], 'gala': [], 'elementaryos': [], 'scratch': [], 'wingpanel': [], 'audience': [], 'pantheon-photos': [], 'wingpanel-indicator-network': [], 'switchboard-plug-notifications': [], 'switchboard-plug-networking': [], 'capnet-assist': [], 'granite': [], 'wingpanel-indicator-notifications': [], 'wingpanel-indicator-datetime': [], 'switchboard-plug-pantheon-shell': [], 'switchboard-plug-applications': [], 'switchboard': [], 'switchboard-plug-a11y': [], 'switchboard-plug-datetime': [], 'midori': [], 'wingpanel-indicator-session': [], 'appcenter': [], 'switchboard-plug-display': [], 'switchboard-plug-keyboard': [], 'pantheon-calculator': [], 'switchboard-plug-power': [], 'pantheon-greeter': [], 'switchboard-plug-mouse-touchpad': [], 'switchboard-plug-locale': [], 'snap-elementary': [], 'switchboard-plug-printers': [], 'slingshot': [], 'switchboard-plug-onlineaccounts': [], 'wingpanel-indicator-bluetooth': [], 'switchboard-plug-security-privacy': [], 'switchboard-plug-about': [], 'wingpanel-indicator-keyboard': [], 'maya': [], 'noise': [], 'pantheon-files': [], 'switchboard-plug-useraccounts': [], 'wingpanel-indicator-sound': [], 'switchboard-plug-parental-controls': [], 'wingpanel-indicator-power': []}}

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
