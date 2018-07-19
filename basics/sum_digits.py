#sum of digits of interger

n = input("Enter a number")
sum = 0

while(n>0):
    digi=n%10
    sum+=digi
    n/=10

print "The sum of digits are :" ,sum