import random

comp_choices = ['rock', 'paper', 'scissors']
comp_hand = comp_choices[random.randint(0,2)]

user_hand = input('rock, paper or scissors?')

while str(user_hand) not in comp_choices:
    print('invalid entry')
    user_hand = input('rock, paper or scissors?')

user_hand = str(user_hand)

if comp_hand == user_hand:
    print('Tie!')

if comp_hand == 'rock':
    if user_hand == 'paper':
        print('You win!')
    if user_hand == 'scissors':
        print('You lose!')

if comp_hand == 'paper':
    if user_hand == 'rock':
        print('You lose!')
    if user_hand == 'scissors':
        print('You win!')

if comp_hand == 'scissors':
    if user_hand == 'rock':
        print('You win!')
    if user_hand == 'paper':
        print('You lose!')

print('PC hand:', comp_hand)
print('Your hand:', user_hand)