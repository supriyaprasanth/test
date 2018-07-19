from Exam import random

words = ['kerala','karnataka','pune','delhi','punjab',]
word = random.choice(words)
word.lower()
length = len(word)
g = []
guessed_word = []
for n in word:
    guessed_word.append('_')
print('The word is')
for i in range(0,length):
    print('_')
for j in range(0,10):
    l=raw_input('Enter the letter')
    l.lower()
    if l in g:
        print('Already Entered')
    else:
        g.append(l)
        if l in word:
            print('Guessed letter is correct')
            for x in range(0,length):
                if word[x]==l:
                    guessed_word[x]=l
            print(guessed_word)
        else:
            print('Letter is not present')
    if not '_' in guessed_word:
        print('Congrats you haved guessed it right!')
        break
if '_' in guessed_word:
    print('Sorry the guess you made is wrong')
