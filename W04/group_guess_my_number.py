# Import the random library
import random

# Ask the user for a magic number
magic_number = random.randint(1, 100)
print(magic_number, '\n')
guess = -1
guess_counter = 0
game_is_on = True

while game_is_on :

    while magic_number != guess:
        guess =  int(input('What is your guess? '))
        guess_counter += 1 # This is the same as guess_counter + 1
        if magic_number > guess:
            print('Higher')
        elif magic_number < guess:
            print('Lower')
        else:
            # print('You guessed it!')
            print(f'You guessed it!\nYou made {guess_counter} geusses.\n')
    # Ask if the user wants to continue playing the game
    want_to_continue = input('Do you want to continue the game? ')
    if want_to_continue.lower() == 'yes':
        magic_number = random.randint(1, 100)
        print(magic_number, '\n')
        guess = -1
        guess_counter = 0
        game_is_on = True
    elif want_to_continue.lower() == 'no':
        game_is_on = False
        print('\nThanks for playing with us today.')
    else: # You cab ignore this part
        print('Please answer YES or NO: \n')