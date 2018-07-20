def pal(str):
    l=len(str)
    n=l
    i=0
    flag=0
    while(n>0):
        if(str[i]!=str[n-1]):
            flag=1
            return flag
        else:
            n=n-1
            i=i+1
    return flag
str=input('Enter the string')
f=pal(str)
if(f==1):
    print('Not a palindrome')
else:
    print('Palindrome')


