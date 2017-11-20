#Вариант3
wordslength1 = 0
wordslength3 = 0
f = open ("/Users/alina/Documents/GitHub/Programming/hw4/texthw.txt",encoding="utf-8")
for line in f:
    words = line.split()
    for i in words:
        if len(i) == 1:
            wordslength1 += 1;
        elif len(i) == 3:
            wordslength3 += 1;
if  wordslength1 == 0:
    print("Нет слов длины 1")
else:
    print("Слов длины 3 больше, чем слов длины 1 в", wordslength3 / wordslength1, "раз")
