# Define the function to check for the first item in a link.
# Below is a simple function
# def initial(word):
#     return word[0:1].upper()

# Using multiple parameters
# def initial(word, force_upper):
#     return word[0:1].upper()

# Using default parameters
def initial(word, forces_upper=True):
    letter = ''
    if forces_upper:
        letter = word[0:1].upper()
    else:
        letter = word[0:1]

    return letter

first_name = input(f'\nFirst name: ')
last_name = input(f'Last name: ')
middle_name = input(f'Middle name: ')
# Regular fuction calling
# print(f'\nYour initials are: {initial(first_name)}{initial(middle_name)}{initial(last_name)}')
# forcing second parameters
# print(f'\nYour initials are: {initial(first_name, False)}{initial(middle_name)}{initial(last_name, False)}')

# The prefered method, named notation
print(f'\nYour initials are: {initial(word=first_name, forces_upper=False)}{initial(word=middle_name, forces_upper=True)}{initial(word=last_name, forces_upper=False)}')


def display_numbers(x, y):
    x = 10

x = 3

y = 4

print(display_numbers(x, y))

'''
Passing parameters to functions
When you define a function, you can declare parameters, which are values that it receives from the place that called it. For example, consider a function print_double that receives a number, doubles it, and prints the result on the screen:


def print_double(value):
    double_value = value * 2
    print(double_value)
Then, you can call this function and pass it any value:


print_double(12) # outputs 24
print_double(3) # outputs 6
print_double(42) # outputs 84




Returning values
Extending the previous example, suppose you want to have the program calculate the double value and return it, instead of printing it to the screen, in case you want to use it in further calculations. In this case, you can use the return statement:


def get_double(value):
    double_value = value * 2
    return double_value
Now the value is given back to the code that called it:


new_number = get_double(4)
The variable new_number would now have the value 8.






Variable Scope
Please be aware that variable names are only valid for the function they are defined in. And, you can even use the name variable name in different functions for different values. This can get a little complicated and you'll see it in much more detail in future classes. But at this point, you need to be aware that whether you use the same variable name or not, the function will have it's own copy of the value. And you can't use it outside of the function.


def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4)

# ERROR: This does not work, because the variable "double_value" is only alive during
# the body of the function. Down here, we have chosen to give the return value the name "new_number"
print(double_value) # BAD CODE
The same concept holds true for parameters:


def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = "Message 1"
print_message(the_message)

# but it also works to use a different variable...
user_message = "Message 2"
print_message(user_message)
In either of the two cases above, when you are in the function, you'll want to use the variable name the_message regardless of what it was called down below.

If this is still a little confusing, that's ok, that's why there is a whole additional course to explore these nuances.


'''