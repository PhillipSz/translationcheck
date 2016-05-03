#!/usr/bin/env python3
#
# Just use "python -m unittest discover -v" to see what happens
#
'''Tests for translationcheck'''
import unittest

from lib import translationcheck

# TODO: Add a test for parseargs(), printit() if possible

class Updateapplists(unittest.TestCase):
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

    def test_if_everything_updated(self):
        '''Test if all files in data/ are updated'''
        results = {'elementary': {}, 'unity-scopes': {}}
        results = translationcheck.getapps(results)
        # We must convert both results and dict_of_apps to a list, because they differ in their structure
        results_list = []
        for project, apps in results.items():
            results_list.append(apps)

        dict_of_apps = translationcheck.updateapplists()
        dict_of_apps_list = []
        for project, apps in results.items():
            dict_of_apps_list.append(apps)

        self.assertEqual(results_list, dict_of_apps_list)

class GetappsTestCase(unittest.TestCase):
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

class GetresultsTestCase(unittest.TestCase):
    '''Tests for getresults().
       I just choose these at random and with the hope that they don't change that much.'''

    # we only test for 0 and error and elnf here, as the rest can change fast
    def test_getresults_elementary(self):
        '''Test the function to parse the webpages for elementary'''

        results_e_de = translationcheck.getresults("pantheon-calculator", "German")
        self.assertEqual(results_e_de, (0, 0))
        results_e_de_error = translationcheck.getresults("this-is-not-an-app-:)", "German")
        self.assertEqual(results_e_de_error, ('error', 'error'))
        results_e_nor = translationcheck.getresults("pantheon-calculator", "Norwegian Bokmal")
        self.assertEqual(results_e_nor, (0, 0))
        results_e_ch = translationcheck.getresults("pantheon-calculator", "Chinese (Simplified)")
        self.assertEqual(results_e_ch, (0, 0))

    def test_getresults_unityscopes(self):
        '''Test the function to parse the webpages for unity-scopes'''

        results_us_de = translationcheck.getresults("unity-scope-remmina", "German")
        self.assertEqual(results_us_de, (0, 0))
        results_us_de_ns = translationcheck.getresults("unity-scope-snappy", "German")
        self.assertEqual(results_us_de_ns, ('lnf', 'lnf'))
        results_us_ch = translationcheck.getresults("unity-scope-remmina", "Chinese (Simplified)")
        self.assertEqual(results_us_ch, ('lnf', 'lnf'))
        results_us_uy = translationcheck.getresults("unity-scope-zotero", "Uyghur")
        self.assertEqual(results_us_uy, (7, 0))
        results_us_al = translationcheck.getresults("unity-scope-click", "Albanian")
        self.assertEqual(results_us_al, (52, 39))

    def test_getresults_ubuntu(self):
        '''Test the function to parse the webpages for ubuntu'''

        results_u_de = translationcheck.getresults("ubuntu-keyboard", "German")
        self.assertEqual(results_u_de, (0, 0))
        results_u_uk = translationcheck.getresults("twitter-scope", "English (United Kingdom)")
        self.assertEqual(results_u_uk, (0, 0))
        results_u_de_error = translationcheck.getresults("nopenotthere", "German")
        self.assertEqual(results_u_de_error, ('error', 'error'))

if __name__ == '__main__':
    unittest.main()
