#!/usr/bin/env python3
#
#

''' Script to check for Launchpad Translation'''
import argparse
from urllib.request import urlopen
import re
import concurrent.futures
import webbrowser
import os
import logging

def parseargs():
    '''Parse the arguments'''
    parser = argparse.ArgumentParser(description='Script to check for Launchpad Translation',
                                     epilog='Report bugs to https://github.com/PhillipSz/translationcheck/issues')
    parser.add_argument("-u", "--ubuntu", help="check ubuntu apps", action="store_true")
    parser.add_argument("-e", "--elementary", help="check elementary apps", action="store_true")
    parser.add_argument("-s", "--unityscopes", help="check unity scopes", action="store_true")
    parser.add_argument("-o", "--open", help="open all untranslated/needs review apps in a browser",
                        action="store_true")
    parser.add_argument("--update", help="checks for new translatable apps \
                         from elementary/unity-scopes and saves them", action="store_true")
    parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")
    parser.add_argument("-l", "--language", type=str, default='German',
                        help='let you specify a language, e.g. German, Greek or "English (United Kingdom)"')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format="%(levelname)s: %(threadName)s: %(message)s", level=logging.INFO)

    if args.update:
        updateapplists()
        raise SystemExit(0)

    results = {}
    if args.ubuntu:
        results["ubuntu"] = {}
    if args.elementary:
        results["elementary"] = {}
    if args.unityscopes:
        results["unity-scopes"] = {}

    if not args.ubuntu and not args.elementary and not args.unityscopes:
        parser.print_help()
        raise SystemExit(1)

    return args.language, args.open, results

def updateapplists():
    '''Updates the list of apps in data/'''
    projects=("elementary", "unity-scopes")
    for project in projects:
        page = urlopen("https://translations.launchpad.net/" + project).read().decode('utf-8')
        page_for_re = page.split('id="untranslatable-projects">')[0]
        regex = '.*https://launchpad\.net/(.*)/\+translations.*'
        res = re.findall(regex, page_for_re)
        if project == "elementary":
            res.append("plank")
        list.sort(res)
        with open('data/' + project, mode='wt', encoding='utf-8') as projectfile:
            projectfile.write('\n'.join(res))
        logging.info("Updated %s.\n", project)

def getapps(results):
    '''Read the projects in'''
    for project in results:
        with open("data/" + project) as project_file:
            for line in project_file:
                results[project][line.rstrip('\n')] = []
    return results

def getresults(app, language):
    '''Download and parse the launchpad pages, to get the numbers'''
    try:
        page = urlopen("https://launchpad.net/" + app + "/+translations").read().decode('utf-8')
    except:
        logging.info("There is something wrong with %s. It is an URLError!\n", app)
        return 'error', 'error'
    # I know I should not parse html with regex, but I still do it because it's easy and the input will always be the same
    regex = '>' + re.escape(language) + '<.*?<img height=.*?<span class="sortkey">([0-9]+)</span>.*?<span class="sortkey">([0-9]+)</span>'
    res = re.search(regex, page, flags=re.DOTALL)
    logging.info("%s downloaded!\n", app)
    try:
        return res.group(1), res.group(2)
    except AttributeError:
        logging.info("We have a problem with parsing %s\n", app)
        # TODO: we must check if this is really the case
        return 'lnf', 'lnf' # language not found

def printit(results, language, openb):
    '''Print it in a fancy way'''
    # colors
    yellow = '\033[93m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

    for project, apps in results.items():
        print("\nFor", project, "in", language, "we have the following results:")

        for app, result in apps.items():
            if result[0] == "error":
                print('\n' + app + ":")
                print(yellow, "There is something wrong with", app + ".\n",
                      "Most likely the projecte moved to a different name.", end)
            elif result[0] == "lnf":
                if openb:
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                print(yellow, "This app probably has no translations in", language, "yet!", end)
            elif result[0] == "0" and result[1] == "0":
                continue
            else:
                if openb:
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                if result[0] != "0":
                    print(red, result[0], "untranslated", end)
                if result[1] != "0":
                    print(green, result[1], "new suggestion(s)", end)

def main():
    '''This main functions calls all other function and also is responsible for running all the downloads at the same time'''
    language, openb, results = parseargs()
    print("Let's see what needs work…")
    results = getapps(results)
    for project, apps in results.items():
        with concurrent.futures.ThreadPoolExecutor(max_workers=(os.cpu_count() or 1) * 5) as executor:
            future_to_app = {executor.submit(getresults, app, language): app for app, rs in apps.items()}
            for future in concurrent.futures.as_completed(future_to_app):
                app = future_to_app[future]
                rest = future.result()
                results[project][app] = rest
    printit(results, language, openb)

if __name__ == "__main__":
    main()
