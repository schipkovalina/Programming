#Вариант3

import os
import collections

def extension():
    extensions = []
    for root, dirs, files in os.walk("."):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            extensions.append(file_extension)
    return extensions

def frequency(e):
    counter = collections.Counter(e).most_common(1)[0][0]
    return counter

def result(c):
    print("Чаще всего встречаются файлы с расширением:", c)

result(frequency(extension()))    


