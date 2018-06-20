#1.(5 баллов). Для каждого файла сделайте следующее: восстановите исходный текст
#(очистите от тегов и знаков ударения) и сохраните его в новый файл с тем же
#названием, но расширением .txt и в кодировке «cp1251». В первой строке нового
#файла напишите название новости, взяв его из тега <title>. 

import re
import os
import collections

def text():
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r = re.compile('<([0-9\D]+)>', line)
    print(f)            

text()

#Нашла еще такой вариант

def cleanhtml():
   for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines(): 
                cleanr = re.compile('<.*?>', line)
                cleantext = re.sub(cleanr, '', line)
  return cleantext

cleanhtml()

#2.(8 баллов). Во всех файлах найдите все имена собственные
#(их леммы должны быть написаны с заглавной буквы) и подсчитайте, сколько раз
#каждое из них встретилось во всей текстовой коллекции. Результаты запишите в
#таблицу со столбцами: найденное имя, количество вхождений. В качестве
#разделителя надо использовать табуляцию.

def names():
    names = []
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                s = re.search('lex="([А-Я][а-я]+)"', line)
                if s:
                    names.append(s.group(1))
    return names

def count(names):
    count = collections.Counter(names)
    return count

def table(c):
    table = []
    with open('names.csv', 'w', encoding='utf-8') as t:
        for word in sorted(c, key=c.get, reverse=True):
            table.append(word + '\t' + str(c[word]))
        table = '\n'.join(table)
        t.write(table)

table(count(names()))
