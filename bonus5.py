def aigpaig():
    a = input("Type a word or a phrase: ") 
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    for i in range(len(a)):
        if a[i] in consonants:
            b = a[i] + "aig"
            print(b, end = "")
        else:
            print(a[i], end = "")


aigpaig()
