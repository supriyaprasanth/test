def dup(l):
    n=[]
    for i in l:
        if i in n:
            continue
        else:
            n.append(i)
    print(n)
k=int(input('Enter the length'))
l=[]
print('Enter the elements')
for j in range(1,k+1):
    a = int(input(''))
    l.append(a)
dup(l)