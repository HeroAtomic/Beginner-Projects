#spagetti code go

import numpy as np
run = True

# Create a random list of numbers between 0 and 100 with a difference of 2 between each number.
number_list = np.arange(0, 101, 2)
number_list = number_list.tolist()

max_index = int(len(number_list))
mid_index = int(len(number_list)/2)
middle_number = int(number_list[mid_index])

# Ask the user for a number between 0 and 100 to check whether their number is in the list.
user_input = input('Pick a number between 1 and 100:')
user_input = int(user_input)

print(number_list)

# The programme should work like this.
# The programme will half the list of numbers and see whether the users number matches the middle element in the list.
# If they do not match, the programme will check which half the number lies in, and eliminate the other half.
# The search then continues on the remaining half, again checking whether the middle element in that half is equal to the user’s number.
# This process keeps on going until the programme finds the users number, or until the size of the subarray is 0, which means the users number isn't in the list.
# Keep going until this is true

while len(number_list) >= 3 and run == True:
    # If this is true we know it is in the bottom half
    if user_input < middle_number:
        number_list = number_list[0:mid_index + 1]
        max_index = int(len(number_list))
        mid_index = int(len(number_list) / 2)
        middle_number = int(number_list[mid_index])
        print(number_list)

    elif user_input > middle_number:
        number_list = number_list[mid_index:max_index]
        max_index = int(len(number_list))
        mid_index = int(len(number_list) / 2)
        middle_number = int(number_list[mid_index])
        print(number_list)

    elif user_input == middle_number:
        run = False

print('\n')

if user_input == middle_number:
    print('Your number is {}'.format(middle_number))

else:
    guess_num = (number_list[1] - 1)
    print('Your number is not in the list...but i know it is {}'.format(guess_num))