class Account:
    #initialised
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance

    #function to deposit
    def deposit(self, amount):
        self.balance=self.balance+amount

    #function to withdraw
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Fund")
        else:
            self.balance=self.balance-amount

    #function to view balance
    def viewbal(self):
        return self.balance

customer1 = Account('A')
customer1.deposit(1000)
print('A')
print( customer1.viewbal())

customer2 = Account('B')
customer2.deposit(1000)
print('B')
print(customer2.viewbal())

customer3 = Account('C')
customer3.deposit(1000)
print('C')
print(customer3.viewbal())

customer4 = Account('D')
customer4.deposit(1000)
print('D')
print(customer4.viewbal())
print("1 CASE")
customer1.withdraw(250)
customer3.deposit(250)
print(customer1.viewbal())
print(customer3.viewbal())
print("2 CASE")
customer1.withdraw(1000)
customer3.deposit(1000)
print(customer1.viewbal())
print(customer3.viewbal())
print("3 CASE")
customer4.withdraw(250)
customer3.deposit(250)
print(customer4.viewbal())
print(customer3.viewbal())
