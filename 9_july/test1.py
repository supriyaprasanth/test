from Exam import random

words = ['kerala','karnataka','pune','delhi','punjab',]
word = random.choice(words)
leng = len(word)
count =0
chances = 9
l_guessed = []
x = ""
y= True
def word_update(x,word, l_guessed):


    for letter in word:
        if letter in l_guessed:
            x += letter
        else: x += " _ "
    print "The word is :", x
    return x

print "Guess the Indian State"

while(y):
    letter = raw_input("Enter a letter : ").lower()
    if letter in l_guessed:
        print "you already entered the letter"
    else:
        l_guessed.append(letter)
        chances-=1
        count+=1
        print " %d more tries left" % (chances)

    if count == leng:
        x = False
        break

    word_update(x, word, l_guessed)


'''while chances >= 0:
    letter = raw_input("Enter a guess: ").lower()
    if letter in l_guessed:
        print "\nYou have already said that!!!\n"
    else:
        l_guessed.append(letter)
        chances = chances - 1
        if x == word:
            print ("tries over")
            break

        print " %d more tries left" % (chances)


    word_update(x,word, l_guessed)
'''


