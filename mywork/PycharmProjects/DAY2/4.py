f=input('Enter the first no')
a=int(f)
s=input('Enter the second no')
b=int(s)
l=input('Enter the third no')
c=int(l)
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>c):
    print(b)
else:
    print(c)


