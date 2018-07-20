str=input('Enter a string')
l=list(str)
n=len(l)
c=0
for j in range(0,n-1):
    if((l[j]=='a')or(l[j]=='A')):
        c=c+1
    else:
        continue
if(c==0):
    print('a is not present in the string ')
else:
    print('a is present',c,'times')