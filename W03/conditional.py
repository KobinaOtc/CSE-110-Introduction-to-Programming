'''
Conditionals are used to write logic where a certain result demands a certian action
The way to start writing a conditional is to us the key word 'if'
Example:

if something == something:
    do_something

The else key word is used to tell the program to execute any other thing that the
if statement did not certify
Example: 

if something == something:
    do_something
else:
    do_something_else

The elif key word is used to write more complex if statements requiring multiple verification
example:
if something_1 == something_2:
    do_something
elif something_1 == something_3:
    do_something_if_correct
else:
    do_something_else

Conditioan combiners like 'or' & 'and' are used to verify multiple conditions
example:

if something == something or something == something_1:
    do_something
elif something == something_2 and something == something_3:
    do_another_thing
else:
    do_something_else

Another combiner which is very useful is the 'in' keyword. I allows you to check is 
multiple outcomes are equal to the value of if statement.
example:

if something in('something_1', 'something_2', 'something_3'):
    do_something
else:
    do_something_else
    
-------------------------------
-------------------------------
if statements can be nested.

Use boolean assignment to save 
execution for later.
The boolean keywords are:
- True
- False
- * Null

example:
if something = something:
    somethingelse = True
else
    somethingelse = False
-------------------------------
-------------------------------

Symbols for verifing conditions:
>  --> Greater than
<  --> less than
>= --> Greater than or equal to
<= --> Less than or equal to
== --> is equal to
!= --> is not equal to
'''
# This is a simple expression of an if statement/ conditional
price = float(input('How much did you pay? '))
tax = 0

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(f'Tax rat is: {tax * 100}%')

# Comparing strings can be tricky, be sure to convert strings to the right case for the best comparism
country = 'CANADA'
# The wrong way to do it:
if country == 'canada':
    print('Oh look a Canadian')
else: 
    print('You are not from Canada')

# The right way to do it
if country.lower() == 'canada':
    print('Oh look a Canadian')
else: 
    print('You are not from Canada')

# Real world practical examples for 'if' Statements
country = input('\nWhat is country are you from? ')

if country.lower() in('ghana', 'nigeria', 'senegal'):
    region = input('What region are you from? ')
    if region.lower() in('edo', 'enugu', 'ibo') and country.lower() == 'nigeria':
        tax = 0.05
    elif region.lower() in('central', 'ashanti', 'accra') and country.lower() == 'ghana':
        tax = 0.15
    else:
        tax = 0.12
else:
    tax = 0

print(f'Your tax rate is: {tax * 100}%\n')