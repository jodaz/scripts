#!/usr/bin/python3
import os
import re
import sys

PATH = input( "PATH: " )
directory = os.path.abspath(PATH)
replace_text = input("Text to replace: ")
new_text = input("New text: ")
count = 0

for foldername, subfolders, filenames in os.walk(directory):
    for file in filenames:
        filepath = foldername + "/" + file
        
        with open(filepath, 'r') as file:
            filedata = file.read()

        filedata = filedata.replace(replace_text, new_text)

        with open(filepath, 'w') as file:
            file.write(filedata)
            count += 1  

print( "\nSuccessful operation, %s files updated!" % count)
