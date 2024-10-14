# Ask users for the Letter
letter = input('\nGuess the word one Letter at a time: ')

# The word Is declared below
word = 'Commitment'

# Run through the work and check for matching 
# letters
for let in word:
    if let.lower() == letter.lower():
        print('_', end = '')
    else:
        print(let.lower(), end = '')

print('\n')