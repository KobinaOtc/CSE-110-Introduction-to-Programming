# Create list for numbers
numbers_list = []
number_entered = None
numbers_total = 0
average = None
largest_number = 0
smallest_number = 99999999999999999999

# Loop for entering numbers
print('\nEnter a list of numbers, type 0 when finished.')
while number_entered != 0:
    number_entered = int(input('Enter number: '))
    if number_entered != 0:
        numbers_list.append(number_entered) # adds numbers to the list
    
    if number_entered > largest_number:
        largest_number = number_entered # sets largest number
    
    if number_entered < smallest_number and number_entered > 0:
        smallest_number = number_entered # Sets smallest number

for number in numbers_list:
    numbers_total += number # Sets total of the list

average = float(numbers_total) / float(len(numbers_list)) # finds average of the list
numbers_list.sort(reverse=False) # Sorts the list

print(f'The sum is: {numbers_total}')
print(f'The average is: {average}')
print(f'The largest number is: {largest_number}')
print(f'The smallest positive number is: {smallest_number}')
print(f'The sorted list is:')
# print the sorted list
for number in numbers_list:
    print(number)

