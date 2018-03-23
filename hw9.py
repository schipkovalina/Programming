# Вариант 3

import re

def text():
    with open("./progtext.txt", "r", encoding = "utf-8") as f:
        words = f.read().lower().split()
    return words

symbols = ".,«»'!?\" \+\=–_[]*:;()^{}><\/|%@#№$•%,1234567890"
    
def search(words):
    forms = []
    for word in words:
        if re.match('программир((у(ю(сь)?|ешь(ся)?|ют(ся)?|ет(ся)?|ете(сь)?|ем(ся)?|й(те(сь)?)?|я(сь)?|))|ова(ть(ся)?)|л(ся|(а|о|и)(сь)?)|(ующ|овавш)(ий|его|ему|им|ем|ая|ей|ую|ее|ие|их|им|ими)(ся)?|овав|(уем|ованн)\
(ый|ая|ое|ого|ом(у)?|ым|ой|ую|ые|ых|ым(и)?))$', word) and word not in forms:
            forms.append(word.strip(symbols))
    else:
        for word in forms:
            print(word + ' ')
    return forms
    
    
search(text())

