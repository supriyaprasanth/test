import re

def validate():
    while True:
        password = raw_input("Enter a password: ")
        if len(password) < 6 or len(password) >12:
            print("Please make sure your password has min 6 and max 12 characters")
        elif re.search('[0-9]',password) is None:
            print("Please use atleast one digit")
        elif re.search('[A-Z]',password) is None:
            print("Please use atleast one capital letter")
        elif re.search('[a-z]', password) is None:
            print("Please use atleast one small letter")
        elif not re.search("[$@#]", password):
            print ("PLease use a special character")
        else:
            print("Valid Password")
            break

validate()
