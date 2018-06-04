#Вариант3

import re
import collections

def file():
    with open("./progtext.txt", "r", encoding="utf-8") as f:
        text = f.read()
    return text

def words(text):
    pattern = re.compile(r'[.|...|…|?|!|\n]') 
    words = {i.strip(): i.split() for i in pattern.split(text) if i}
    return words

def word(words):
    for value in words.values():
        for i in value:
            i = i.strip("1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& ()")
            print("{}_{}".format(i, str(len(i))))

    
word(words(file()))
    

