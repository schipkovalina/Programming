#Вариант3

import random

def hint():
    d = {}
    with open("./wordhint.csv", 'r', encoding='utf-8') as f:
        for line in f:
             word, hint = line.strip().split(" ", maxsplit=1)
             d[word] = hint
    return d


def programm(dictionary):
    tries = 0
    key = random.choice(list(dictionary))
    print("Эта программа загадывает слова,которые нужно угадать по подсказке.\n\
Количество попыток = количество букв в подсказке.\n\
Подсказка:", dictionary[key]," ...")
    guess = input("Загаданное слово: ")
    while guess.lower() != key and tries < len(dictionary[key])-1:       
        print("Ответ неправильный,но еще", len(dictionary[key])-1-tries, "попыток.")
        guess = input("Загаданное слово: ")
        tries += 1
    if tries == len(dictionary[key])-1:
        print("Попытки закончились. Загаданное слово: ", key)
    if guess.lower() == key:
        print("Правильный ответ!")    


programm(hint())

