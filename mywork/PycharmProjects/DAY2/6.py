a=input('Enter a number')
n=int(a)
flag=1
for j in range(2,int(n/2),1):
    if(n%j==0):
        flag=0
        break
if(flag==0):
    print(n,'is not a prime no')
else:
    print(n,'is a prime no')
