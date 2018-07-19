import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = input("enter the length of the password")
p =  "".join(random.sample(s, passlen))
print p