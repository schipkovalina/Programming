n = 0
with open("D:\Downloads\Ozhegov.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split('|')
        if words[2] != '':
            n += 1
print(n)
