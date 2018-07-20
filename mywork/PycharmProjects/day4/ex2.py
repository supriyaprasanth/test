l=[1,2,1,3,2,1,2,2,3,3,1]
s=[]
n=len(l)
for i in l:
    cn=0
    if i not in s:
        for j in range(0,n):
            if i==l[j]:
                cn=cn+1
        print(i,':',cn)
        s.append(i)