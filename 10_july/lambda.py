n=input("enter the number of elements : ")
item  = []
for i in range(0,n):
    a = input("enter the items : ")
    item.append(a)

squared=map(lambda x:x*x, item)
print squared



