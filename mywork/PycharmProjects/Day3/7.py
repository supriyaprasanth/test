s=input('Enter the string')
l=s.split(' ')
n=[]
for i in(l):
    if i in n:
        continue
    else:
        n.append(i)
print(n)