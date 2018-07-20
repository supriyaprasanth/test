class account:
    def __init__(self,):
        self.balance=0
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Fund")
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def viewbal(self):
        print(self.balance)
A=account()
B=account()
C=account()
D=account()
l=[A,B,C,D]
a='Y'
while a=='y'or a=='Y':
    n=int(input('Enter the account holder'))
    print('1.Withdrawal')
    print('2.Deposit')
    print('3.ViewBalance')
    ch=int(input('Enter the choice'))
    if ch==1:
        amt=int(input('Enter the amount to be withdrawn'))
        l[n].withdraw(amt)
    elif ch==2:
        amt=int(input('Enter the amount to be deposited'))
        l[n].deposit(amt)
    else:
        l[n].viewbal()
    a=input("More?")

