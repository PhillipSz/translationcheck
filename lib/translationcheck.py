''' Lib to check for Launchpad Translation'''
import re
import webbrowser
import logging
import configparser
import os
import sys
from copy import deepcopy

try:
    import requests
except ImportError:
    print('Please install requests with "sudo pip3 install requests"!')
    raise SystemExit(1)

if sys.version_info <= (3, 5):
    raise "You must use python 3.5 or greater! Sorry!"

def readconfig():
    '''Reads the config file and also askes if there is none'''
    config = configparser.ConfigParser()
    config.read('.conf.ini')

    try:
        language = config['DEFAULT']['language']
    except KeyError:
        language = input("Please enter your language (can be changed later in '.conf.ini'): ")
        config['DEFAULT']['language'] = language
        with open('.conf.ini', 'w') as configfile:
            config.write(configfile)

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
        return int(res.group(1)), int(res.group(2))
    except AttributeError:
        logging.info("We have a problem with parsing %s\n", app)
        return 'lnf', 'lnf' # language not found

def chart(results):
    ''''Opens a new tab with a translation chart from the results.
        If multiple projects are given it will put it all together'''
    projects = []
    ut = []
    nr = []
    usefull_results = deepcopy(results) # we must use deepcopy here, because otherwise we will get an runtime error

    for project, apps in results.items():
        for app, result in apps.items():
            if result[0] in (0, "error", "lnf") and result[1] in (0, "error", "lnf"):
                del usefull_results[project][app]

    for project, apps in usefull_results.items():
        for app, result in apps.items():
            projects.append(app)
            ut.append(result[0])
            nr.append(result[1])

    projects = 'labels : ' + str(projects) + ','
    ut = ','.join(str(e) for e in ut)
    ut = 'data : [' + ut + ']'
    nr = ','.join(str(e) for e in nr)
    nr = 'data : [' + nr + ']'

    # Parts of this code are from https://github.com/chartjs/Chart.js/blob/master/samples/bar-horizontal.html which is MIT
    page1 = '''
        <!doctype html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Horizontal Bar Chart</title>
            <script src="Chart.min.js"></script>
        </head>

        <body>
            <div id="container" style="width: 90%;">
                <canvas id="canvas"></canvas>
            </div>

            <script>

                var horizontalBarChartData = {
        '''

    page2 = '''
            datasets: [{
                label: 'untranslated',
                backgroundColor: "rgba(20, 25, 238, 0.7)",
                '''
    page3 = '''},
            {
                label: 'needs review',
                backgroundColor: "rgba(236, 11, 32, 0.7)",
                    '''

    page4 = '''}]

            };
                window.onload = function() {
                    var ctx = document.getElementById("canvas").getContext("2d");
                    window.myHorizontalBar = new Chart(ctx, {
                        type: 'horizontalBar',
                        data: horizontalBarChartData,
                        options: {
                            responsive: true,
                            legend: {
                                position: 'top',
                            },
                            title: {
                                display: true,
                                text: 'Translations Chart'
                            }
                        }
                    });

                };

            </script>
        </body>
        </html>
    '''

    with open("data/diagram.html", 'w') as html_file:
        html_file.write(page1 + projects + page2 + ut + page3 + nr + page4)

    webbrowser.open("file://" + os.getcwd() + "/data/diagram.html")

def printit(results, language, openb):
    '''Print it in a fancy way'''
    # colors
    def print_red(*text):
        print('\033[91m', *text, '\033[0m')
    def print_green(*text):
        print('\033[92m', *text, '\033[0m')
    def print_yellow(*text):
        print('\033[93m', *text, '\033[0m')

    for project, apps in results.items():
        print("\nFor", project, "in", language, "we have the following results:")

        for app, result in apps.items():
            if result[0] == "error":
                print('\n' + app + ":")
                print_yellow("There is something wrong with", app + ".\n",
                             "Most likely the project moved to a different location.")
            elif result[0] == "lnf":
                if openb:
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                print_yellow("This app probably has no translations in", language, "yet!")
            elif result[0] == 0 and result[1] == 0:
                continue
            else:
                if openb:
                    webbrowser.open("https://launchpad.net/" + app + "/+translations")
                print('\n' + app + ":")
                if result[0] != 0:
                    print_red(result[0], "untranslated")
                if result[1] != 0:
                    print_green(result[1], "new suggestion(s)")
