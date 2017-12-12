with open("D:\Downloads\Ozhegov.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        words = line.split('|')
        vocword = words [0]
        if len(vocword) >=20:
            print (line)
        
