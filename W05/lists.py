'''
list notes:
List methods.
1. .append('item' or variable): the append keyword is used to add items onto the end list
of a list.
----------------------------------------------------------------------------------
example:

some_list = ['something']
some_list.append('something_else')
print(some_list) # this will display ['somthing', 'somthing_else']

more examples:
books = []

books.append("1 Nephi")
books.append("2 Nephi")
books.append("Jacob")
books.append("Enos")

Iterat through each item:
print("Your books are:")

for book in books:
    print(book)
----------------------------------------------------------------------------------

AVOID MIXING DATA TYPES WITHIN LISTS!!!

Working with numbers:
With list you can easily work with numbers by runing them through a for loop. Many iterations
of the loop could perform various mathematical functions. Below is an example of a simple sum loop
----------------------------------------------------------------------------------
Example 1:

loop = [1, 2, 3, 4]
loop_sum = 0
for num in loop:
    loop_sum += num
print(loop_sum) # Displays 10

Example 2:

receipts = [12.24, 18.50, 4.99, 21.75]

running_total = 0

for receipt in receipts:
    running_total = running_total + receipt

# Display the total
print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48
----------------------------------------------------------------------------------
A new operator
As you saw in the previous example, we can add to a variable with code like this:


age = 30
age = age + 1

print(age) # This displays: 31
But because this is so common, there is an operator that can do this in one step. This is done using the += operator:


age = 30
age += 1

print(age) # This displays: 31
These two versions do the same thing, but people generally prefer to use the += operator because it's simpler, easy to understand, and less prone to mistakes.

With this in mind, the previous code example could be updated to be the following:


for receipt in receipts:
    # Note the use of the += operator here
    running_total += receipt
'''

friend_names = []
name = ''

while name != 'end':
    name = input('Type the name of a friend: ')
    if name != 'end':
        friend_names.append(name)

print('\nYour friends are:')
for friend_name in friend_names:
    print(friend_name)
