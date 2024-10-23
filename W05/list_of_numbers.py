'''
Author: 01 CSE 110 Thursday 8am MT
Purpose: List of Numbers
'''

# Declare the variables for storing the numbers and list
entered_number = None
list_of_numbers = []
num_total = 0
average = 0
largest_number = 0
smallest_number = 999999999999999

print('\nEnter a list of numbers, type 0 when finished.')
while entered_number != 0: # While the entered number is not equal to 0 then apend the entered number into the list
    entered_number = int(input('Enter number: '))
    if entered_number != 0:
        list_of_numbers.append(entered_number)
    
    if entered_number > largest_number:
        largest_number = entered_number
    
    if entered_number < smallest_number and entered_number > 0:
        smallest_number = entered_number

for number in list_of_numbers:
    num_total += number

average = float(num_total) / float(len(list_of_numbers)) # Finding the avarege of the numbers in the list
list_of_numbers.sort(reverse=False) # Stretch challenge used to sort the list

print(f'The sum is: {num_total}\nThe average is: {average}\nThe largest number is: {largest_number}\nThe smallest positive number is: {smallest_number}\nThe sorted list is:')

for number in list_of_numbers:
    print(number)
