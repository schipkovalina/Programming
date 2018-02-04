#Вариант3

import re

def openfile():
    i = str(input("Введите название файла с английским текстом: "))
    file = "./" + i + ".txt"
    with open(file, encoding="utf-8") as f:
        f = f.read()
        f = list(filter(None, re.split('\W', f)))
        return f


def hoodsearch(f):
    freq = {}
    for x in range(len(f)):
        if f[x][-4::] == "hood" or f[x][-5::] == "hoods":
            if f[x] in freq:
                freq[f[x]] += 1
            else:
                freq[f[x]] = 1
    return freq


def wordamount(freq):
    wordamount_list = sum(list(freq.values()))
    return wordamount_list


def minfreq(freq):
    volume = list(freq.values())
    key = list(freq.keys())
    return key[volume.index(min(volume))]


def wordgen(freq):
    wordgen_list = []
    for word in freq:
        if word[-6::] == "lihood":
            wordgen_list.append(word[0:-6:])          
        elif word[-4::] == "hood":
            wordgen_list.append(word[0:-4:])
        else:
            wordgen_list.append(word[0:-5:])  
    return wordgen_list


def main():
    print("Существительных с суффиксом -hood в тексте: " + str(wordamount(hoodsearch(openfile()))))
    print("Существительное с минимальной частотностью: " + str(minfreq(hoodsearch(openfile()))))
    print("Слова, от которых образованы существительные с суффиксом -hood: " + str(wordgen(hoodsearch(openfile()))))
    
if __name__ == "__main__":        
    main()


