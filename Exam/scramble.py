from Exam import random

f = open("ex.txt",'r+') # to open the file containing the text to scrambleble
new = open("ex2.txt", 'r+') # a file to write the scramblebled text
print f.read() #to read the original file containing the text
f.seek(0) # to start reading the file from the beginning
s = []

line = f.read().split()
for x in range(0,len(line)):
    s[x] = str(line(x))
    for i in line:
        if len(line) > 3:
            print "testing if"
            x = len(line) - 1
            first = word[0]
            last = word[len(line)-1]
            second = word[1]
            word = list(word)

            mix = ""
            index = 0
            scrambled = ""

            for k in range(second,len(word) - 2):
                index = random.randint(1, (x - 1))
                mix = mix + i[index]
                i.pop(index)
                x = x - 1
            scrambled = first + mix + last
            new.write(scrambled)
        else:
            print "inside else"





