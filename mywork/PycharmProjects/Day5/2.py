def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)

n=int(input('Enter the number'))
if n==0:
    print('Factorial of no is :1')
elif(n<0):
    print('no factorial')
else:
    print('Factorial of no is:',fact(n))
