intostring=input("enter your introducton")
print(intostring)  
charactercount=0
wordcount=1

for i in intostring:
    charactercount=charactercount+1
    if(i==' '):
        wordcount=wordcount+1

print("no of words in the strings ")
print (wordcount)
print("no of character in the strings ")
print (charactercount) 

