import random

tries = 0

number = random.randint(0,20)
user_guess = input('Guess a number between 0 and 20:')
tries += 1

while int(user_guess) != number:
    if int(user_guess) > 20:
        print('Number is out of range! Pick a number between 1 abd 20')
        user_guess = input('Guess a number:')
    elif int(user_guess) > number:
        print('Number is too high!')
        user_guess = input('Guess a number:')
        tries += 1
    elif int(user_guess) < number:
        print('Number is too low!')
        user_guess = input('Guess a number:')
        tries += 1

print('You win! It took you {} tries'.format(tries))