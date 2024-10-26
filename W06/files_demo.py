'''
Opening a file in python
The simplest way to do that is to set the variable and call the open function on it.
example:
variable = open('file')

The above is the old way of of opening files. That way requires that the file be closed
using the close fuction
example:
variable.close()

The new convention encouraged is to use the with key word to create a block in which the 
code is run:
with open('file') as variable:
    perform programs here

Working with strings
using the split function 
example:
string_variable = 'one two three'
string_split = string_variable.split()
# string_split = ['one', 'two', 'three']

Handling white spaces
In python there is an in built fuction used to clear white spaces ie: strip
example:
string_with_white_space = '-----    the string     -----'
clean_string = string_with_white_space.strip()
# clean_string = '-----the string-----'


Finding the Max or Min
Recall from previous lessons that a way to find the largest number in a list is to keep track of the largest number found to date, and then update that value if you find a new one that is larger. For example:


numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # This number is larger than the largest we had seen so far

        # So it is now the largest we've seen
        largest_so_far = number

# Now, after the loop we can display it:
print(f"The largest is: {largest_so_far}")
This produces the following output:


The largest is: 85
It is important to remember to start the largest_so_far variable at either the first value (assuming it's not an empty list) or else something that you know will be smaller than everything in your list. Otherwise, you won't consider some numbers. For example, if you started it at 10, then you would never consider anything less than 10.

Keeping track of the item that is the Max or Min
What if you want to know not only which number is the largest, but also the item that is the largest? For example, you may want to know not only the most expensive price in your shopping cart, but the actual product that is the most expensive. The logic above will only find the largest value. To find the largest item, you'll also need to keep track of its name or value along the way.

Consider the following list of products in a shopping cart, along with their prices:


shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]
In order to find the most expensive price, we can iterate through it as before:


max_price = -1

for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")
This produces the following output:


The maximum price is: 6.99
If we want to find the name of the item that is the most expensive, we need to declare a variable (for example, max_product) before the loop to keep track of the product that had the maximum price. Then, whenever we update the max_price to save a new price, we also update the max_product to be the corresponding product name. For example:


max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")
This produces the following output:


The maximum price is: 6.99
The product with the maximum price is: Ice Cream


'''

# Write with block to open file.

with open('courses.txt') as course_file:
    # for line in course_file:
    #     print(line)
    # print()
    for line in course_file:
        line = line.strip()
        split_line = line.split(',')
        course = split_line[0]
        grade = float(split_line[1])
        print(f'{course} Grade: {grade:.2f}\nGrade after bonus: {grade + 3:.2f}\n')

print()

# Working with strings
colors = 'red yellow blue green'
color_parts = colors.split() # Split colors into list
# color_parts = ['red', 'yellow', 'blue', 'green']

# Loop to print each color from the split list
for color in color_parts:
    print(color)
