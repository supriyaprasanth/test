n=[]
k=input('enter the limit')
l=int(k)
for j in range(1,l+1):
    a = input('enter the element')
    n.append(a)
n.sort()
print(n[l-1])
