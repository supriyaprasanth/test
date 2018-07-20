import re
email=input('Enter the email')
mob=input('Enter the mobile no')
age=input('Enter the age')

match=re.search(r'\w+@\w+.\w+',email)
if match:
    print('valid')
else:
    print('Invalid')

m2=re.search(r'\d{10}',mob)
if(m2):
    print("valid")
else:
    print("invalid")

m3=re.search(r'^(0?[0-9]?[0-9]|1[0][0])$',age)
if(m3):
    print("valid")
else:
    print("Invalid")
