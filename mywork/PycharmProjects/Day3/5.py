s=input('Enter the words')
l=s.split(',')
k=len(l)
l.sort()
for j in range(0,k):
    print(l[j],end=',')

