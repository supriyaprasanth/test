str=input('Enter the string')
k=str.split(' ')
s=[]
n=len(k)
for i in k:
    cn=0
    if i not in s:
        for j in range(0,n):
            if i==k[j]:
                cn=cn+1
        print(i,':',cn)
        s.append(i)