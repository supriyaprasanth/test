pwd=input('Enter the password')
n=s=u=l=0
if (len(pwd)<6)or(len(pwd)>12):
    print('Not a valid length')
else:
    for c in pwd:
        if c.isdigit():
            n=1
        elif(c=='$'or c=='@'or c=='#'):
            s=1
        elif c.isupper():
            u=1
        elif c.islower():
            l=1
    if n==1 and s==1 and u==1 and l==1:
        print('valid password')
    else:
        print('invalid password')