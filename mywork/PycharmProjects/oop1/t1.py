class employee:

    #sets the values
    def setemp(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary

    #initialising
    def __init__(self):
        first=''
        last=''
        salary=0

    #to get fullname
    def getfullname(self):
        full=first+last
        return full

    #to get email
    def getemail(self):
        email=first+'.'+last+'@inapp.com'
        return email

    #to get total salary
    def getsal(self):
        tsal=salary*12
        return tsal

emp=employee()
first=input("Enter the first name")
last=input("Enter the last name")
salary=int(input("Enter the salary"))
print(emp.getfullname())
print(emp.getemail())
print(emp.getsal())
