#!  python3
# deleteFiles.py - Delete all files matched against a regex pattern

# TODO: Add Linux support.

import os, re, sys

dir_path = input('Directory: ')
directory = os.listdir(dir_path)

pattern = input('Regex pattern: ')
regex = re.compile(r'%s'%pattern)
files = [('%s\\%s' % 
            (dir_path, file)) for file in directory if regex.search(file)]

def delete_files(file_paths):
    for file in file_paths:
        print('Removing %s' % file)
        os.remove(file)

if len(files) == 0:
    print("No files found.")

print('-------------- File Samples --------------')
for file in files[:10]:
    print(file)

confirm = input('Do you want to delete these files? (Y/N): ')
if confirm.lower() == 'y': delete_files(files)

input("Press ENTER to quit.")
