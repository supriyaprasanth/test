def reverse(str):
    n=len(str)
    str1=''
    while(n>0):
        n=n-1
        str1=str1+str[n]
    print(str1)
str=input('Enter the string')
reverse(str)
