s=input('Enter the string')
l=len(s)
flag=0
n=l
i=0
while(n>0):
    if(s[i]!=s[n-1]):
        flag=1
        break
    else:
        i=i+1
        n=n-1
if(flag==0):
    print('Its a palindrome')
else:
    print('Its not a palindrome')
