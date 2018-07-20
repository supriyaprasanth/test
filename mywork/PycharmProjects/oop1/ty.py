class account:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance=balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient Fund")
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def viewbal(self):
        return self.balance

accA=account('A')
accB=account('B')
accC=account('C')
accD=account('D')
c='y'
print("1.Transfer 250 from  A to C")
print("2.Transfer 1000 from A to D ")
print("3.Transfer 250 from D to C ")


    choice=input()
    if(choice==1):
        a=int(input("Enter the amount"))