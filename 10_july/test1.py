f = open('example.txt','r+')
new_file = open ('new.txt','w+')
for line in f:
    if 'a' in line:
        new_file.write(line.replace('a','/a'))
    else:
        print("character not found")






