# a program that walks through a folder tree and searches for files with a 
# certain extension. copy these files from wherever they are into a new dir.

import os
import shutil

DEST_PATH = 'C:\\Users\\h4yb33\\codemongers'
warning = r'''
     Usage:  py filedel.py 'C:\Users\codemonger\desktop' - absolute path
             py filedel.py '..\desktop'  - relative path'''

while True:
    search_path = input('Enter path to crawl: ')
    if os.path.exists(search_path) and os.path.isdir(search_path):
        print(search_path)
        break
    else:
        print(warning)

for foldername, subfolders, filenames in os.walk(search_path):
    for sub in subfolders:
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.pdf' or os.path.splitext(filename)[1] == '.jpg':
            if not os.path.exists(DEST_PATH):
                os.mkdir(DEST_PATH)

            print(os.path.realpath(filename))
    else:   # when it encounters a non 'jpg' or 'pdf' just skip
        continue