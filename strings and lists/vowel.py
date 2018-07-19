c=raw_input("Enter a letter : ")
vowel="aeiouAEIOU"

if c in vowel:
    print c," is a vowel"
else:
    print c," is NOT a vowel"


c=raw_input("Enter a letter :")
a=c.translate(None,"aeiouAEIOU")
print(a)
