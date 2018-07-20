x=30
def add(x):
    x=x+15
    print(x)
    print(id(x))
add(x)
print(x)
print(id(x))
print('\n')
l=[1,2,3,4,5]
print(id(l))
def addval(l):
    l[4]=6
    print(id(l))
addval(l)
print(l)