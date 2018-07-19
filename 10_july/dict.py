f = open('courses.txt','r+')
r = f.read().split()
l = len(r)
dict = {i:r[i] for i in range (0,l)}
print dict
f.close()