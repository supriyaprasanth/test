import random
w=["rock","paper","scissors"]
play='y'
cm=us=0
while play=='y':
    u=input()
    c=random.choice(w)
    print(c)
    if(u==c):
        play=input('Play Again')
        continue
    elif(u=='rock'and c=='paper'):
        cm=cm+1
    elif(u=='paper'and c=='rock'):
        us=us+1
    elif(u=='scissors'and c=='paper'):
        us=us+1
    elif(u=='paper'and c=='scissors'):
        cm=cm+1
    elif(u=='rock'and c=='scissors'):
        us=us+1
    else:
        cm=cm+1
    play=input('Play Again')
if(cm>us):
    print('Computer Wins')
elif(us>cm):
    print('User Wins')
else:
    print('There is a tie')
