cust_details={1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}
print(cust_details)
del cust_details[1005]
print(cust_details)
cust_details[1003]="Anne"
print(cust_details)
if 1002 in cust_details:
    print("Yes it exists")
else:
    print("No it does not exists")