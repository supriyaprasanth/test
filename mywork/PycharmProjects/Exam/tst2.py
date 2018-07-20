import random
min=1
max=100
n=random.randint(min,max)
i=1
flag=0
while(i<=5):
    guess=int(input('Enter the guess'))
    d=n-guess
    if(d==0):
        print('Congratzzzz You got it right')
        flag=1
        break
    elif(d>0):
        if(d<10):
            print('You are closer Try a bigger no')
        elif(d<20):
            print('Try a larger no')
        else:
            print('You are far from the no try bigger')
    else:
        f=guess-n
        if (f < 10):
            print('You are close Try a smaller no')
        elif (f < 20):
            print('Try a smaller no')
        else:
            print('You are far from the no try smaller')
    i=i+1
if(flag==0):
    print('Oops Sorry Try next time the no is',n)