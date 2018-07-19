str = raw_input("Enter a phrase : ")
word = str.split()

from collections import Counter
wordcount = Counter(word)
print dict(wordcount)
#print(wordcount)