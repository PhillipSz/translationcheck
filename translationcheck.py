#!/usr/bin/env python3
#
# TODO:
#   - make it possible to update the app list files
#   - maybe add debugging options?
#   - add (unit?)tests
#

''' Script to check for Launchpad Translation'''
import argparse
from urllib.request import urlopen
import re
import concurrent.futures
import webbrowser
import os

def parseargs():
    '''Parse the arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--ubuntu", help="check ubuntu apps", action="store_true")
    parser.add_argument("-e", "--elementary", help="check elementary apps", action="store_true")
    parser.add_argument("-s", "--unityscopes", help="check unity scopes", action="store_true")
    parser.add_argument("-o", "--open", help="open all untranslated/needs review apps in a browser",
                        action="store_true")
    parser.add_argument("-l", "--language", type=str,
                        help='let you specify a language, e.g. German, Greek or "English (United Kingdom)"')
    args = parser.parse_args()

    results = {}
    if args.ubuntu:
        results["ubuntu"] = {}
    if args.elementary:
        results["elementary"] = {}
    if args.unityscopes:
        results["unityscopes"] = {}
    if args.language:
        language = args.language
    else:
        language = "German"
    if args.open:
        openb = "1"
    else:
        openb = "0"

    return language, openb, results

def getapps(results):
    '''read the projects in'''
    for project in results:
        with open("data/" + project) as f:
            for line in f:
                results[project][line.rstrip('\n')] = []
    return results

def getresults(app, language):
    '''Download and parse the launchpad pages, to get the numbers'''

    page = urlopen("https://launchpad.net/" + app + "/+translations").read().decode('utf-8')
    # I know I should not parse html with regex, but I still do it because it's easy and the input will always be the same
    regex = '>' + language + '<.*?<img height=.*?<span class="sortkey">([0-9]+)</span>.*?<span class="sortkey">([0-9]+)</span>'
    res = re.search(regex, page, flags=re.DOTALL)
    #print (app, "downloaded!")
    try:
        return res.group(1), res.group(2)
    except AttributeError:
        return 'error', 'error'

def printit(results, language):
    '''Print it in a fancy way'''
    # colors
    yellow = '\033[93m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

    for project, apps in results.items():
        print("\nFor", project, "in", language, "we have the following results:")

        for app, rs in apps.items():
            if rs[0] == "error":
                if openb == "1":
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                print(yellow, "This app probably has no translations in", language, "yet!", end)
            elif rs[0] == "0" and rs[1] == "0":
                continue
            else:
                if openb == "1":
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                if rs[0] != "0":
                    print(red, rs[0], "untranslated", end)
                if rs[1] != "0":
                    print(green, rs[1], "new suggestion(s)", end)

if __name__ == "__main__":
    language, openb, results = parseargs()
    print("Let's see what needs work…")
    results = getapps(results)
    for project, apps in results.items():
        with concurrent.futures.ThreadPoolExecutor((os.cpu_count() or 1) * 5) as executor:
            future_to_app = {executor.submit(getresults, app, language): app for app, rs in apps.items()}
            for future in concurrent.futures.as_completed(future_to_app):
                app = future_to_app[future]
                rest = future.result()
                results[project][app] = rest
    printit(results, language)
