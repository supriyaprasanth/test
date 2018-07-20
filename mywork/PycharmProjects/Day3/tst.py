s = input('Enter the string')
l1 = s.split(' ')
c=len(l1)
for j in range (0,c):
    cn=1
    for i in range (j+1,c):
        if(l1[j]==l1[i]):
            cn=cn+1
            continue
        else:
            continue
    print(l1[j], ':', cn)