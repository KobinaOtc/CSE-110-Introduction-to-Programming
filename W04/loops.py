'''
Loops are used to iterate over a specific out come until a desired
out come is achieved.
example:

number = 0

while number < 10:
    ask_for_number = input('ask for a number higher than 10: ')
    number = int(ask_for_number)

Loop will stop once the user inputs a number greater than 10
'''
# First loop activity
# Ask user for a number

number = int(input('\n\nPlease type a positive number: '))

while number < 0: # while the numbe is less than 10 the loop will run
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Please type a positive number: '))

print(f'The number is: {number}')

# Second loop activity
# While the answer is no keep runing the loop

answer = input('\nMay I have a piece of candy? ')

while answer.lower() != 'yes':
    answer = input('May I have a piece of candy? ')

print('Thank you\n\n')
