#!/usr/bin/env python3
#
# Just use "python -m unittest discover -v" to see what happens
#
'''Tests for translationcheck'''
import unittest
# ugly hack to import translationcheck
# from http://stackoverflow.com/questions/4542352/import-from-sibling-directory
import os
import inspect
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

import translationcheck

# TODO: Add a test for parseargs(), printit() if possible

class updateapplists(unittest.TestCase):
    '''Tests for updateapplists'''
    def test_updateapplists(self):
        '''Test if we get an empty dict back (don't know if that test is useful) '''
        dict_of_apps = translationcheck.updateapplists()
        self.assertTrue(dict_of_apps)
        self.assertTrue(isinstance(dict_of_apps, dict))

    def test_check_if_false_app_elementary(self):
        '''Test if the function does gives us an elementary app that is not translatable'''
        dict_of_apps = translationcheck.updateapplists()

        for project, apps in dict_of_apps.items():
            if project == 'elementary':
                # test if the first and last app in the list is there.
                # this should test the regex
                self.assertFalse('contractor' in apps)
                self.assertFalse('wingpanel-indicator-a11y' in apps)
                self.assertTrue('scratch' in apps)
                self.assertTrue('switchboard' in apps)

    def test_check_if_false_app_unityscopes(self):
        '''Test if the function does gives us a unity scope that is not translatable'''
        dict_of_apps = translationcheck.updateapplists()

        for project, apps in dict_of_apps.items():
            if project == 'unity-scopes':
                self.assertTrue('unity-scope-isgd' in apps) # it's called: "Unity is.gd Scope" that's why we should test that
                self.assertTrue('unity-scope-zotero' in apps)
                self.assertTrue('unity-scope-ubuntushop' in apps)
                self.assertFalse('unity-scope-snappy' in apps)
                self.assertFalse('unity-scope-piratebay' in apps)

class getappsTestCase(unittest.TestCase):
    '''Tests for getapps.'''

    def test_get_apps(self):
        '''Test the function to parse the apps to check'''

        results = {'elementary': {}, 'ubuntu': {}, 'unity-scopes': {}}
        results = translationcheck.getapps(results)
        self.assertTrue('elementary' and 'ubuntu' and 'unity-scopes' in results)

        for project, apps in results.items():
            if project == 'ubuntu':
                self.assertTrue('ubuntu-system-settings-online-accounts' in apps)
                self.assertTrue('unity8' in apps)
            if project == 'elementary':
                self.assertTrue('switchboard-plug-parental-controls' in apps)
                self.assertTrue('plank' in apps)
            if project == 'unity-scopes':
                self.assertTrue('unity-scope-isgd' in apps)
                self.assertTrue('unity-scope-zeitgeistwebhistory' in apps)
                self.assertTrue('unity-scope-zotero' in apps)

class getresultsTestCase(unittest.TestCase):
    '''Tests for getresults().
       I just choose these at random and with the hope that they don't change that much.'''

    # we only test for 0 and error and elnf here, as the rest can change fast
    def test_getresults_elementary(self):
        '''Test the function to parse the webpages for elementary'''

        results_e_de = translationcheck.getresults("pantheon-calculator", "German")
        self.assertEqual(results_e_de, ('0', '0'))
        results_e_de_error = translationcheck.getresults("this-is-not-an-app-:)", "German")
        self.assertEqual(results_e_de_error, ('error', 'error'))
        results_e_nor = translationcheck.getresults("pantheon-calculator", "Norwegian Bokmal")
        self.assertEqual(results_e_nor, ('0', '0'))
        results_e_ch = translationcheck.getresults("pantheon-calculator", "Chinese (Simplified)")
        self.assertEqual(results_e_ch, ('0', '0'))

    def test_getresults_unityscopes(self):
        '''Test the function to parse the webpages for unity-scopes'''

        results_us_de = translationcheck.getresults("unity-scope-remmina", "German")
        self.assertEqual(results_us_de, ('0', '0'))
        results_us_ch = translationcheck.getresults("unity-scope-remmina", "Chinese (Simplified)")
        self.assertEqual(results_us_ch, ('lnf', 'lnf'))

    def test_getresults_ubuntu(self):
        '''Test the function to parse the webpages for ubuntu'''

        results_u_de = translationcheck.getresults("ubuntu-keyboard", "German")
        self.assertEqual(results_u_de, ('0', '0'))
        results_u_uk = translationcheck.getresults("ubuntu-keyboard", "English (United Kingdom)")
        self.assertEqual(results_u_uk, ('0', '0'))

if __name__ == '__main__':
    unittest.main()
