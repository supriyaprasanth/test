#largest of 3 numbers

n1=input("Enter first number")
n2=input("Enter second number")
n3=input("Enter third number")
int(n1)
int(n2)
int(n3)

if(n1>n2):
    if(n1>n3):
        print("largest is", n1)
elif(n2>n3):
    print("latgest is", n2)
else:
    print("largest is", n3)