#Вариант3

import re

def openfile():
    with open( "./linguistics.html", "r", encoding="utf-8") as f:
        article = f.read()
#        result = re.sub('язык(а|у|ом|е|и|ов|ам|ами|ах)?', 'шашлык(а|у|ом|е|и|ов|ам|ами|ах)?', article)
#        result = re.sub('Язык(а|у|ом|е|и|ов|ам|ами|ах)?', 'Шашлык(а|у|ом|е|и|ов|ам|ами|ах)?', result)
        result = re.sub(r'(\W|^)язык(а|у|ом|е|и|ов|ам|ами|ах)?(-|\W|$)', r'\1шашлык\2\3', article)
        result = re.sub(r'(\W|^)Язык(а|у|ом|е|и|ов|ам|ами|ах)?(-|\W|$)', r'\1Шашлык\2\3', result)
        return result
    
def write(result):
    with open("./shashlik.txt", 'w', encoding='utf-8') as t:
        t.write(result)
    
write(openfile())

