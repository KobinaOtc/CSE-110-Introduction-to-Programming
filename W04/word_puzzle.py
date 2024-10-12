'''
Author: Brother Otchere
Purpose: Word Puzzle
'''
# Import the random library, Stretch challenge
import random

# Stretch challenge words in a list
words = ['temple', 'mosiah', 'moroni', 'father', 'mother', 'nephi', 'helaman', 'zion', 'alma']
# Define the secret word
secret_word = words[random.randint(0, 8)]
# Define hint
hint = ''
for i in secret_word:
    hint += '_'

# Welcome message
print('\nWelcome to the word guessing game!\n')
# Check for letter match
print(f'Your hint is: {hint}')
guess = ''
guess_count = 0
guess_lives = 3
# Stretch challenge - add a while loop to check for the number of times left to guess
while guess.lower() != secret_word and guess_lives > 0:
    guess = input('What is your guess? ').lower()
    hint = ''
    guess_count += 1
    guess_lives -= 1
    if len(guess) == len(secret_word):
        for i, letter in enumerate(guess):
            if letter == secret_word[i]:
                hint += letter.upper()
            elif letter != secret_word[i]:
                is_in = ''
                for let in secret_word: # Check for letter match
                    if letter == let:
                        is_in = letter.lower()
                if is_in != '':
                    hint += is_in
                else:
                    hint += '_'
        print(f'Your hint is: {hint}\nYou have {guess_lives} lives left') # Stretch add the number of lives yet
    else:
        print(f'Sorry, the guess must have the same number of letters as the secret word.\nYou have {guess_lives} lives left\n')

if guess.lower() == secret_word:
    print(f'\nCongratulations! You guessed it!\nIt took you {guess_count} guesses.\n')
else: # Stretch challenge
    print(f'\nSorry the secret word was {secret_word}\n\nGAME OVER!!\nYou runout of lives!!\n')