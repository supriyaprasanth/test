from Exam import random

words = ('kerala','karnataka','pune','delhi','punjab',)
word = random.choice(words)
chances = 10
l_guessed = []
hidden = ["_"]*len(word)


def word_update(word, l_guessed):

    hidden = " "
    for letter in word:
        if letter in l_guessed:
            hidden += letter
        else: hidden += " _ "
    print "The word is :", hidden
    return hidden
print "Guess the Indian State"

while chances != 0:
    letter = raw_input("Enter a guess: ")
    letter.lower()
    if letter in l_guessed:
        print "\nYou have already said that!!!\n"
    else:
        l_guessed.append(letter)
        chances = chances - 1
        print " %d more tries left" % (chances)
        if hidden == word:
            break
    word_update(word, l_guessed)


word_guesses = 1
word_guess = 0


if word_guesses == 1:
    print "One more chance...."
else:
    print "%d tries left." % (word_guesses)
while word_guess != word_guesses:
    guess = raw_input("Guess the word: ").lower()
    if guess ==  word:
        print "Correct, the word is %s!" % (guess)
        break
    else:
        print "Nope."
    word_guess += 1
    if  word_guess == word_guesses:
        print "Sorry. No more tries %s." % (word)
