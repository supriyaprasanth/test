file=open("course.txt","r+")
print(file.read())
file.seek(0)
dic={}
i=0
l=file.read().split()
for j in l:
    dic[i]=j
    i=i+1
print(dic)