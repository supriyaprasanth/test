str=raw_input("enter the string : ")
output = []


for word in str.split():
    if word not in output:
        output.append(word)

str=' '.join(output)
print str


