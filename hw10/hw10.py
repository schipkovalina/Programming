#Вариант 3

import re

def openfile():
    with open("./wiki.html", "r", encoding="utf-8") as f:
        for line in f:
            s = re.search('data-wikidata-property-id="P571".*>(\d+)', line)
            if s:
                data = s.group(1)
                return data
            
def write(year):
    with open("./text.txt", "w", encoding="utf-8") as t:
        result = "Год основания: " + year
        t.write(result)
        
write(openfile())
