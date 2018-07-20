import random
class rps:
    def __init__(self):
        self.us=0
        self.cm=0

    def cmpch(self):
        l=['rock','paper','scissors']
        self.cmp=random.choice(l)
        print(self.cmp)

    def usch(self,choice):
        self.user=choice

    def game(self):

        if (self.user== 'rock' and self.cmp == 'paper'):
            self.cm = self.cm + 1
        elif (self.user == 'paper' and self.cmp == 'rock'):
            self.us = self.us + 1
        elif (self.user == 'scissors' and self.cmp == 'paper'):
            self.us = self.us + 1
        elif (self.user == 'paper' and self.cmp== 'scissors'):
            self.cm = self.cm + 1
        elif (self.user == 'rock' and self.cmp == 'scissors'):
            self.us = self.us + 1
        elif (self.cmp == 'rock' and self.user == 'scissors'):
            self.cm = self.cm + 1

    def won(self):
        if(self.us>self.cm):
            print("Congratzzz You Won")
        elif(self.us<self.cm):
            print("Sorry Computer Won")
        else:
            print("Oops there is a tie")

gam=rps()
n='y'
while(n=='y'or n=='Y'):

    choice=input('Enter Choice')
    gam.usch(choice)
    gam.cmpch()
    gam.game()
    n=input("Play More?")

gam.won()

