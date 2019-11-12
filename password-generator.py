# Password Generator
# Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be, and how many letters
# and numbers they want in their password. Have a mix of upper and lowercase letters,
# as well as numbers and symbols. The password should be a minimum of 6 characters long.

import string
import random

def generate_password():
    letters_all = string.ascii_lowercase + string.ascii_uppercase
    letter_list = []
    for letter in letters_all:
        letter_list.append(letter)

    print(len(letter_list))

    def ask(what):
        user_input = input('How many {} would you like your password to be?'.format(what))
        return user_input

    characters = ask('characters')
    while  int(characters) < 6:
        print('Password is too short')
        characters = ask('characters')

    letters = ask('letters')
    numbers = ask('numberss')
    while int(letters) + int(numbers) != int(characters):
        print('Wrong amount of chracters. Total length is {}'.format(characters))
        letters = ask('letters')
        numbers = ask('numberss')

    my_password = []

    for char in range(int(letters)):
        #the length is 1 indexed, the list is 0 indexed
        random_number = random.randint(0,len(letter_list)-1)
        current_letter = letter_list[random_number]
        my_password.append(current_letter)

    for number in range(int(numbers)):
        random_number = random.randint(0,9)
        my_password.append(random_number)

    random.shuffle((my_password))
    #print(my_password)

    PASSWORD = ''

    print('\n')

    for i in my_password:
        PASSWORD += str(i)

    print('Your password is: {}'.format(PASSWORD))
    return(PASSWORD)

generate_password()
