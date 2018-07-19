# r p s 2 player game
from Exam import random

words = ["r","p" ,"s"] #list of words
chances = 1

p1 = p2 =0  #to store the score
print "rock = r \n scissor = s \n paper = p \n"

while chances <= 5: # for 10 chances
    print chances
    player1 = raw_input("Player 1 : ")  #getting input from user
    #print player1
    player2 = random.choice(words)   # random play by computer
    print "Player 2 : " ,player2
    #print player2

    if(player1 == player2):    #scoring rules of the game
        p1+=1
        p2+=1
    elif(player1 == 'r' and player2 == 's'):
        p1+=1
    elif(player1 == 's' and player2 == 'r'):
        p2+=1
    elif(player1 == 's' and player2 == 'p'):
        p1+=1
    elif(player1 == 'p' and player2 == 's'):
        p2+=1
    elif(player1 == 'p' and player2 == 'r'):
        p1+=1
    elif(player1 == 'r' and player2 == 'p'):
        p2+=1

    chances +=1

if(p1 > p2):
    print "\nPlayer 1 WINS!!!!"
elif(p1 < p2):
    print "\nPlayer 2 WINS!!!!"
elif(p1 == p2):
    print "Tie match"

print "\nplayer1 scored %d" %(p1)
print "\nplayer2 scored %d" %(p2)




















































