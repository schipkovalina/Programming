def kirpich():
    a = input("Введите слово или фразу: ")
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    for i in range(len(a)):
        if a[i] in vowels:
            b = a[i] + "с" +  a[i]
            print(b, end = "")
        else:
            print(a[i], end = "")
        

kirpich()
