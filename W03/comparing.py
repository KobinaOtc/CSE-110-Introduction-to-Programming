# Ask for the 2 numbers required.
num_1 = float(input('What is the first number? '))
num_2 = float(input('What is the second number? '))

# First if statement check if the first number is greater than the second number.
if num_1 > num_2:
    print('The first number is greater')
else:
    print('The first number is not greater')

# Second if statment check if the numbes are equal or not.
if num_1 == num_2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

# Third if statement check if the second number is greater than the first number.
if num_2 > num_1:
    print('The second number is greater')
else:
    print('The second number is not greater')

# Compare strings by asking users for their favorite animal and comparing it to yours.
my_favorite_animal = 'Dog'
your_favorite_animal = input('\nWhat is your favorite animal? ')
# if statement to compare strings.
if my_favorite_animal.lower() == your_favorite_animal.lower():
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')