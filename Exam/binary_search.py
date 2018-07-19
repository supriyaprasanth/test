# to do binary search
n=input("enter the number of elements : ")  # to get the number of elements
item  = []

for i in range(0,n):   #to accept the elements of the list
    a = input("enter the items : ")
    item.append(a)

print item

ele = input("Enter the element to be searched :") # to accept the element to be searched

first = item[0]
last = item[n-1]
if n%2 == 0: #to find the middle element of the list
    mid =  n / 2
else:
    mid = (n-1) / 2

if ele == item[mid]:
    print "element found at index %d" %(mid+1)
elif ele < item[mid]:
    for i in range(0,mid-1):
        if ele == item[i]:
            print "element found at index %d" %(i+1)
elif ele >item[mid]:
    for i in range(mid,n):
        if ele == item[i]:
            print "element found at index %d" %(i+1)




