str = raw_input("Enter some words seperated using ,  : ")
words = str.split(",")
words.sort()

for i in words:
   print(i)