import random
min=1
max=6
roll='y'
us=0
cm=0
while roll=='y':
    print('Start')
    u=random.randint(min, max)
    print(u)
    us=us+u
    c=random.randint(min, max)
    print(c)
    cm=cm+c
    roll=input('play again')
if(us>cm):
    print("User wins")
else:
    print("Computer wins")




