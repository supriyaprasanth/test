n=[]
k=int(input('enter the limit'))
for j in range(1,k+1):
    a = int(input('enter the element'))
    n.append(a)
n.sort()
p=int(input('Enter the no to be searched'))
for i in range(0,k):
    fi=0
    la=k-1
    while(fi<=la):
        mid=int((fi+la)/2)
        if(p==n[mid]):
            break
        elif((p>n[fi])and (p<n[mid])):
            la=mid-1
        else:
            fi=mid+1
print(p,'is at',mid+1,'position')




