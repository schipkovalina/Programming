def piglat():
    a = input("Type a word or a phrase: ")
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    if a[0] in consonants and a[1] not in consonants:
        b = a[1:] + a[0]
        print(b + "ay")
    if a[0] in consonants and a[1] in consonants:
        c = a[2:] + a[0] + a[1]
        print(c + "ay")
    if a[0] in vowels:
        d = a[0:]
        print(d + "way or", a + "ay")

piglat()


