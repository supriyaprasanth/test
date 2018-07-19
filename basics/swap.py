# swapping without temp variables

n1=input("Enter first number : ")
int(n1)
n2=input("Enter the second number : ")
int(n2)

print (" before swapping:n1 is:",n1," n2 is:",n2)

n1+=n2
n2=n1-n2
n1-=n2

print ("After swapping: n1 is:",n1," n2 is:",n2)
