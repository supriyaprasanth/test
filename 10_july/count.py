f = open('count.txt','r+')
dict = {}
word = f.read().split()
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1
print dict
f.close()