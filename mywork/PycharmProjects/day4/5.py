import random
words=["anne","india","malayalam","beautiful","system","wealth","safety","badminton"]
word=random.choice(words)
word.lower()
length=len(word)
g=[]
gw=[]
for n in word:
    gw.append('_')
print('The word is')
for i in range(0,length):
    print('_',end=' ')
for j in range(0,10):
    l=input('Enter the letter')
    l.lower()
    if l in g:
        print('Already Entered')
    else:
        g.append(l)
        if l in word:
            print('Correct guess')
            for x in range(0,length):
                if word[x]==l:
                    gw[x]=l
            print(gw)
        else:
            print('Incorrect Guess')
    if not '_' in gw:
        print('User wins')
        break
if '_' in gw:
    print('Sorry You Lose')

