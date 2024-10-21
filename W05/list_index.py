'''
Accessing items in a list via their index
You can access an item in a list at a given index via the square bracket [] notation:


first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

-----------------------------------------------------------------------------------------------------------------------

Finding the size of the list
You can find out how many elements are in a list, by using the len function (which is short for length) as follows:


number_of_books = len(books)
-----------------------------------------------------------------------------------------------------------------------

Iterating through a list using an index
In previous lessons, you learned how to iterate through each item in a list using a standard for loop. Another way to do 
this is to have the loop iterate through the indexes 0 through the size of the list, and then access each item using the 
[] notation:

for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen.
Looking a little closer at that for loop you can see that len(books) gets the number of items in the list, and then the 
for i in range(...): part iterates through the numbers 0, 1, 2, 3, ..., up until (but not including) the size of the 
list. So if the list has 10 elements, this will loop through from 0–9, which are the exact indexes you want.
-----------------------------------------------------------------------------------------------------------------------

Printing indexes
If you want to print the index numbers next to the elements of the list as you iterate through, you can print the value 
of the i variable:


for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}")
But be careful. Don't forget that the indexes will start at 0. If you want to display these numbers in a more 
user-friendly manner, you may need to add 1 to the variable i when you display it.
-----------------------------------------------------------------------------------------------------------------------

Working with parallel lists

The most common solution to this problem is to loop through the indexes that correspond to one of the lists and then you
 can access the item from each list at that index:


names = []
numbers = []

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")
-----------------------------------------------------------------------------------------------------------------------

Removing items from a list
There are a few different ways to remove items from a list in Python, but the easiest is to use the "pop" function to 
pop the item out of the list. You tell the pop function the index of the item you want to remove. If you don't give it 
an index, it will remove the last one:


the_list.pop(3) # Removes the item at index 3

the_list.pop() # Removes the last item
'''
# Print shopint lists
print('\nPlease enter the items of the shopping list (type: quit to finish):')
items = []
item = None

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        items.append(item)

print('\nThe shopping list is:')
for i in range(len(items)):
    print(items[i])

print('\nThe shopping list with indexes is:')
for i in range(len(items)):
    print(f'{i}. {items[i]}')

item_change_index = int(input('\nWhich item index would you like to change? '))
new_item = input('What is the new item? ')
items[item_change_index] = new_item # Better method

## Long method
# for i in range(len(item)):
#     if i == item_change_index:
#         items[i] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(items)):
    print(f'{i}. {items[i]}')

