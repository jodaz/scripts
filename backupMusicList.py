#! python3
# backupMusicList.py - create a data backup from a music tracks directory.

# TODO: List all tracks in directory and subdirectories.

# TODO: Save all names in a .json file.

""" IDEAS:
    -   Update records.
    -   Remove records if they do not exist currently and if user allows it.
"""

import os

dirname = input("Path: ")

if not os.path.exists(dirname): print('Path %s doesn\'t exist' % dirname)

input('Press ENTER to exit.')