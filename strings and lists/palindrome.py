str=raw_input("enter a string to check whether it's palindrome : ")

str_rev=str[::-1]

if(str==str_rev):
    print "The string is a palindrome"
else:
    print "string is NOT a palindrome"