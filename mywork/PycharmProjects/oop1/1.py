class employee:
    def __init__(self,firstname,lastname,salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
    def getfullname(self):
        return "%s %s" % (self.firstname, self.lastname)
    def getemail(self):
        return "%s.%s@inapp.com" %(self.firstname,self.lastname)

    def getsal(self):
        return self.salary*12



emp=employee("Anne Mary","David",50000)
print(emp.getfullname())
print(emp.getemail())
print(emp.getsal())