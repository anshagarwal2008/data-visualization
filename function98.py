def CountWordsfromfile():
    filename=input("Enter The File Name ")
    file=open(filename, 'r')
    
    numberofwords=0
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print("number of words ")
    print(numberofwords)

CountWordsfromfile()    