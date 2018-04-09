#Вариант1

#import re

def openfile():
    with open("D:\Downloads\isltext.xml", "r", encoding="utf-8") as f: 
        corpus = f.read()
        lines = 0
        for string in corpus:
            while string != "</teiHeader>":
                lines += 1
            return lines

openfile()            
        
#        lines = 0
#        for string in corpus:
 #           if string != "</teiHeader>":
  #              lines += 1
#            else:
#                break 
#            print(lines)
#        xml = re.search("</teiHeader>", f)   
 

    
    
        
