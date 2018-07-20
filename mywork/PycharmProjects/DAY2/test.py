n=input('Enter the limit')
l=int(n)
print('Enter the array')
for i in range(0,l):
    a=input()
for i in range(0,l-2):
    if a[i]>a[i+1]:
        max=a[i]
        a[i+1]=a[i]
    else:
        max=a[i+1]
print(max,'is the largest of the array')


