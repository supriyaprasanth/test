a=input('Enter the integer')
num=int(a)
s=0
while (num>0):
    r=int(num%10)
    s=s+r
    num=int(num/10)
print (s)

