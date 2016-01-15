''' Lib to check for Launchpad Translation'''
import re
import webbrowser
import logging
import configparser

try:
    import requests
except ImportError:
    print('Please install requests first with "sudo pip install requests"!')
    raise SystemExit(1)

def readconfig():
    config = configparser.ConfigParser()
    config.read('.conf.ini')
    language = config['DEFAULT']['language']
    if not language:
        language = input("Please enter your language (can be changed later in '.conf.ini'): ")
        config['DEFAULT']['language'] = language
        with open('.conf.ini', 'w') as configfile:
            config.write(configfile)
        return language
    else:
        return language

def updateapplists():
    '''Updates the list of apps in data/'''
    print("Updating... ")
    dict_of_apps = {"elementary": [], "unity-scopes": []}

    for project, _ in dict_of_apps.items():
        page = requests.get("https://translations.launchpad.net/" + project).text
        page_for_re = page.split('id="untranslatable-projects">')[0]
        regex = r'.*https://launchpad\.net/(.*)/\+translations.*'
        res = re.findall(regex, page_for_re)
        if project == "elementary":
            res.append("plank")
        list.sort(res)
        dict_of_apps[project] = res

    return dict_of_apps

def getapps(results):
    '''Read the projects in'''
    for project in results:
        with open("data/" + project) as project_file:
            for line in project_file:
                results[project][line.rstrip('\n')] = []
    return results

def getresults(app, language):
    '''Download and parse the launchpad pages, to get the numbers'''
    page = requests.get("https://launchpad.net/" + app + "/+translations")
    if page.status_code != 200:
        logging.info("There is something wrong with %s. Status Code=%s!\n", app, page.status_code)
        return 'error', 'error'
    else:
        page = page.text
    # I know I should not parse html with regex, but I still do it because it's easy and the input will always be the same
    regex = '>' + re.escape(language) + '<.*?<img height=.*?<span class="sortkey">([0-9]+)</span>.*?<span class="sortkey">([0-9]+)</span>'
    res = re.search(regex, page, flags=re.DOTALL)
    logging.info("%s downloaded!\n", app)
    try:
        return res.group(1), res.group(2)
    except AttributeError:
        logging.info("We have a problem with parsing %s\n", app)
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
                      "Most likely the project moved to a different location.", end)
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
