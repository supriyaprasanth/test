fl1=open('test.txt','r+')
fl2=open('test2.txt','r+')
d={}
l=fl1.read().split()
for c in l:
    if c not in d:
        d[c] = 1
    else:
        d[c]=d[c]+ 1
print(d)

fl2.write(str(d))
