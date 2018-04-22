#Вариант3

import os
import re

def search():
    folders = []
    for folder in os.listdir():
        if os.path.isdir(folder):
            dirpath, filename = os.path.split(folder)
            r = re.search('[a-zA-Z0-9]|[,—\[\]↑№!\"\'«»?.,;:-|/+*{}<>@#$%-^&()]', filename)
            if not r:
                folders.append(filename)
    return folders
            
def count(folders):
    print("Папок, название которых состоит только из кириллических символов:", int(len(folders)))

count(search())

