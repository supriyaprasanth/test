def sq(x):
    return x*x
n=input("enter the number of elemenst ; ")
item  = []
for i in range(0,n):
    a = input("enter the items : ")
    item.append(a)

#item =[1,2,3,4]

squared = map(sq,item)
print squared
