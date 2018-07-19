f = open('count.txt','+')
dict = {}
#word = f.split()
for i in f:
    for word in i.split(' '):
        word = word.strip('.').strip()
        if(word in dict):
            dict[word] = dict[word] + 1
        else:
            dict[word] = 0

print(dict)