from Exam import random


def word_update(word, letters_guessed): #
    masked_word = ""
    for letter in word:
        if letter in letters_guessed:
            masked_word += letter
        else: masked_word += "-"
    print "The word:", masked_word
# List of words for the computer to pick from
words = ("basketball", "football", "hockey", "lacrosse", "baseball")
# Word to be guessed; picked at random from "words"
word = random.choice(words)
guesses = 10 # You can change this; it's how many letter guesses the user gets
letters_guessed = []
print "="*32
print "      Guess the sport!"
print "You get to guess %d letters." % (guesses)
print "There are %s letters in the word." % (len(word))
print "="*32
while guesses != 0:
    letter = raw_input("Enter a letter: ").lower()
    # Doesn't use up a guess if the user has already guessed that letter
    if letter in letters_guessed:
        print "You already guessed that letter."
    else:
        guesses = guesses - 1
        print "You have %d guesses left." % (guesses)
        letters_guessed.append(letter)
    word_update(word, letters_guessed)
word_guesses = 1 # number of guesses to guess the word
word_guess = 0 # current guess number
if word_guesses == 1:
    print "You get 1 guess to guess the word."
else:
    print "You get %d guesses to guess the word." % (word_guesses)
while word_guess != word_guesses:
    guess = raw_input("Guess the word: ").lower()
    if guess ==  word:
        print "Congratulations, %s is the word!" % (guess)
        break
    else:
        print "Nope."
    word_guess += 1
    if  word_guess == word_guesses:
        print "You ran out of tries!\nThe word was %s." % (word)
print "\nThanks for playing LaMouche's Word Guess Game."
