#!/usr/bin/env python3
#

''' Script to check for Launchpad Translation'''
import argparse
import logging
import concurrent.futures
import os

from lib import translationcheck as tc

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
    parser.add_argument("-l", "--language", type=str,
                        help='let you specify a language, e.g. German, Greek or "English (United Kingdom)". \
                              If you have not specified a language, the configuration from ".conf.ini" will be used.')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format="%(levelname)s: %(threadName)s: %(message)s", level=logging.INFO)

    results = {}
    if args.ubuntu:
        results["ubuntu"] = {}
    if args.elementary:
        results["elementary"] = {}
    if args.unityscopes:
        results["unity-scopes"] = {}

    if not args.ubuntu and not args.elementary and not args.unityscopes and not args.update:
        parser.print_help()
        raise SystemExit(1)

    return args.update, args.language, args.open, results

def main():
    '''This main function calls all other functions and also is responsible for running all the downloads at the same time'''
    update, language, openb, results = parseargs()

    if update:
        dict_of_apps = tc.updateapplists()

        for project, apps in dict_of_apps.items():
            with open('data/' + project, mode='wt', encoding='utf-8') as projectfile:
                projectfile.write('\n'.join(apps))
            logging.info("Updated %s.\n", project)
        print("Done!")

    if results:
        print("Let's see what needs work…")

        if not language:
            language = tc.readconfig()

        if language.islower():
            print('Error: You must capitalize the language, just as they are written in launchpad!\n' +
                  'Either specify a valid language with -l or change your language in ".conf.ini".')
            raise SystemExit(1)

        results = tc.getapps(results)
        for project, apps in results.items():
            with concurrent.futures.ThreadPoolExecutor(max_workers=(os.cpu_count() or 1) * 5) as executor:
                future_to_app = {executor.submit(tc.getresults, app, language): app for app, _ in apps.items()}
                for future in concurrent.futures.as_completed(future_to_app):
                    app = future_to_app[future]
                    rest = future.result()
                    results[project][app] = rest
        tc.printit(results, language, openb)

if __name__ == "__main__":
    main()
