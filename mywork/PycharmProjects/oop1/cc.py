class account:
    def __init__(self,balance=0):
        self.balance=balance
    def __withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Fund")
        self.balance=self.balance-amount

    def __deposit(self,amount):
        self.balance = self.balance + amount

    def viewbal(self):
        return self.balance


d={}
acc=account()
c='y'
balance=0
print("1.WITHDRAWAL")
print("2.DEPOSIT")
print("3.VIEW BALANCE")
print("4.ADD ACCOUNT")

while (c=='y'):
    choice=input('Enter Choice')
    if(choice=='1'):
        print ("Withdraw money from Account.")
        number = input("Accoutnnumber: ")
        if number in d:
            w = float(input("How much money would you like to withdraw?"))
        d[number].withdraw(w)

    elif (choice == '2'):
        print("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in d:
            dep = float(input("How much money would you like to deposit? > "))
        d[number].deposit(dep)
    elif(choice=='3'):
        print('View balance of')
        number=input("Accountnumber: ")
        acc.viewbal()
    elif(choice=='4'):
        print("Enter a new Accountnumber")
        numb = input("New accountnumber: ")
        d[numb] = balance
        print("Accountnumber", numb, "opened.")

    c=input("Any More?")