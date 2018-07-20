import random
file = open('text.txt','r+')
nwfile = open('text2.txt','r+')
print(file.read())
file.seek(0)

#checks the length of the word
def chklength(i):
    if len(i) > 3:
        return 1
    else:
        return 0


#function to scramble the words
def scramble(i):
    l = len(i)
    m = l-1
    first = i[0]
    last = i[m]
    i = list(i)
    scram = ""
    index = 0
    nwwrd = ""
    for j in range(len(i)-2):
        index = random.randint(1,(m-1))
        scram = scram + i[index]
        i.pop(index)
        m = m-1
    nwwrd = first + scram + last
    return nwwrd


#to write to the new file
def filewrite (scram) :
    nwfile.write(scram)
    nwfile.write(" ")
res = ""
scam = ""
line = file.read().split()

for i in line:
    res = chklength(i)
    if (res == 1):
        scram = scramble(i)
        filewrite(scram)
    else:
        scram = i
        filewrite(scram)

