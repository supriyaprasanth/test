from Exam import random

file = open('ex.txt','r+')
nwfile = open('ex1.txt','r+')
print(file.read())
file.seek(0)



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
        index = random.randint(1, (m - 1))
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

    if len(i)>3:
        scram = scramble(i)
        filewrite(scram)
    else:
        scram = i
        filewrite(scram)
