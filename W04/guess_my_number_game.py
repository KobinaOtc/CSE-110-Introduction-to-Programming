'''
Author: Team Activity
Purpose: Guess my number game
'''
# Import random library
import random

# Ask user for the magic number
magic_num = random.randint(1, 100)
# Declare the variable number to guess
number_guessed = -1
guesses = 0
play_game = 'yes'
print()
# Stretch task
while play_game == 'yes': # Write loop for checking if the player still wants to play
    # Write loop for checking for the number
    while magic_num != number_guessed:
        number_guessed = int(input('What is your guess? '))# Ask user for a number guess
        if number_guessed > magic_num: # Check if number is higher or lower than the magic number
            print('Lower') 
        elif number_guessed < magic_num:
            print('Higher')
        
        guesses += 1 # Guess counter, add one to what guesses is
    print(f'\nYou guessed it! The magic number is {magic_num}\nYou made {guesses} guesses\n') # Print results
    play_game = input('\nDo you want to play again? ') # Ask user if they want to play again.
    if play_game.lower() == 'yes': # Check if the user wants to continue playing
        guesses = 0
        number_guessed = -1
        magic_num = random.randint(1, 100)
    elif play_game.lower() == 'no': 
        print('\nThanks for playing the game\n')
    else:
        play_game = input('Answer yes or no? ')

