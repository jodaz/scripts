#! python3
#  indexbuilder.py — build an json file of current html files in dir
""" TODO:
    -  Fix import to dbpages.js
    -  Open browser window after compilation.
"""

import os
import sys
import json

dbpages = {}

for file in os.listdir():

    if file.startswith('index'):
        print("Ignoring index.html")
        continue

    if file.endswith('.html'):

        url = file.replace(' ', '%20')
        filename = file.replace('.html', '')

        dbpages.setdefault(filename, url)

if not len(dbpages):
    sys.exit( "No html files found in dir %s" % os.getcwd())
else:
    print("Found %s html files" % len(dbpages))

with open('dbpages.js', 'w') as db:
    json.dump(dbpages, db, indent=2)

input("PRESS ENTER TO QUIT")
