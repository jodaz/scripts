#!/usr/bin/python3
from os.path import isdir
from os import listdir
from os import remove
import re
import sys

PATH = input( "PATH: " )

# Check the PATH
# Remember the syntax is /home/user
while True:
    if isdir( PATH ):
        break
    else:
        sys.exit( "Error" )

# List the files in PATH, then search last letters
for f in listdir( PATH ):
    x = re.findall( ".+.([a-z0-9][a-z0-9][a-z0-9])", file )

    # Discrimine by mp3, flac and m4a
    # If does not match, answer user to delete
    if x != ['mp3'] and x != ['lac'] and x != ['m4a']:
        user = input( 'Do you want to remove %s? Y/N: ' % file ).lower()

        if user == "y":
            print( "...Deleting %s..." % file )
            remove( PATH + "/" + file )

        if user == "n":
            print( "Save", file )

print( "\nSuccefull operation!" )
