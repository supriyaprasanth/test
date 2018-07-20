str=input('Enter the phrase')
l=str.split(' ')
s=[]
for i in (l):
    if i in(s):
        continue
    else:
        print(i,':',l.count(i))
        s.append(i)

