#Вариант3
word = input('Введите слово ')
print(word)
for i in range(0, len(word)-1):
    a = []
    a.append(word[1:])
    a.append(word[0])
    b="".join(a)
    word = b
    print(b)

