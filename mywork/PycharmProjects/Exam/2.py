import random
min=1
max=100
n=random.randint(min,max)
i=1
flag=0

while(i<=5):
    # inputs the guess
    gues=input('Enter the guess')

    #checks whether the guess made is a number
    if(gues.isdigit()!=1):
        print('Please enter a no')
    else:
        guess=int(gues)

        #compute the difference between guess and original
        d=n-guess

        #when guess matches the number you win
        if(d==0):
            print('Congratzzzz You got it right')
            flag=1
            break

        #when guess made is smaller than the number
        elif(d>0):
            if(d<10):
                print('You are closer Try a bigger no')
            elif(d<20):
                print('Try a larger no')
            else:
                print('You are far from the no try bigger')

        #when guess made is larger than the number
        else:
            f=guess-n
            if (f < 10):
                print('You are close Try a smaller no')
            elif (f < 20):
                print('Try a smaller no')
            else:
                print('You are far from the no try smaller')

    i=i+1

#when all the 5 tries are exhausted game is over
if(flag==0):
    print('Oops Sorry Try next time the no is',n)