import re
str="Hello John your customer id is j234"

c=len(str)
if(re.match(r'hello John',str,re.I)):
    print("true hello preceeds john")
else:
    print("false")

if(re.match(r'[a-z][0-9]{3}$',str)):
    print("true")
else:
    print("false")


if(re.search(r' [a-z][0-9]{3}$',str)):
    position=str.find('j',c-4,c)

    res=re.sub(r'[a-z][0-9]{3}$',str[position+1:],str)
    print(res)


match=re.sub('id','ID',str)
print(match)







