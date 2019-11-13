# Hangman loves spagetti for lunch
# The user needs to guess letters,
# Give the user no more than 6 attempts for guessing wrong letter.
# This will mean you will have to have a counter.
# You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a random word to use.

import urllib.request
import random

word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

word = words[random.randint(0, len(words))]
word = word.lower()
starting_word = word

def hide_word():
    # find the length of the word
    length = len(word)
    # create a word that is --- same length
    # needs to be accessed by other functions
    global hidden_word
    hidden_word = []
    for i in word:
        hidden_word.append('-')
    #the hidden word is now created
    print(hidden_word)

def user_guess():
    global guess_left
    # Let the user guess a letter
    guessed_letter = input('Guess a letter:')
    guessed_letter = guessed_letter.lower()

    #check if it has already been guessed
    if guessed_letter in guessed_letters:
        print('You already guessed {}!'.format(guessed_letter))
    #if not continue
    else:
        guessed_letters.append(guessed_letter)
        # Now lets check if the letter is in the wordm if it is, do something
        how_many = word.count(guessed_letter)
        if guessed_letter in word:
            for i in range(how_many):
                # If it is, we will finx out the index
                index = fake_word.index(guessed_letter)
                # Then we replace the - with the letter
                hidden_word[index] = guessed_letter
                # we need to remove it from the fake word and then do this again
                fake_word[index] = '_'
        else:
            guess_left -= 1
            print('Sorry, {} is not the in the word'.format(guessed_letter))
            print('{} wrong guesses remaining'.format(guess_left))


# We want the oringal word to be immutable
word = tuple(word)
#print(word)
# Using lists we need a fake word to find all the indexes of repeated letters
fake_word = list(word)
#print(fake_word)

# Start out by hiding the word
hide_word()

guess_left = 6
guessed_letters = []

# go until the word is guessed
# or until 6 guesses are done
while list(word) != hidden_word and guess_left !=0:
    user_guess()
    print(hidden_word)

if guess_left == 0:
    print('You lose! The word was {}'.format(starting_word.upper()))
else:
    print('You win! The word, as you know was {}'.format(starting_word.upper()))
