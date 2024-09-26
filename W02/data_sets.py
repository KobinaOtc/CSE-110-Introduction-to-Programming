# Converting strings to numbers

# Adding 2 number strings will result in adding the 2 strings side by side
num_1 = '5'
num_2 = '6'

print(num_1 + num_2)
# Print = '56'

# convert the strings to intigers
num1 = int(num_1)
num2 = int(num_2)

num3 = float(num_1)
num4 = float(num_2)

print(num1 + num2)
# the print results will be 11
print(num3 + num4)
# print = 11.0 because it is a float

# All Number Operations:

# Addition
add = num1 + num2
# Subtraction
sub = num1 - num2
# Multipliction
mul = num1 * num2
# Division
div = num1 / num2
# Divide & Drop Remender
div_drop = num1 // num2
# Exponent
expo = num1 ** num2
# Modulus
modl = num1 % num2



# Converting Numbers to strings
for_display = str(add)
# str() is used to convert numbers to strings
print(for_display + ' is the result of adding 5 and 6')

# Best way to print numbers is to use the string format --> pass the number down throw the {}
print(f'this is a number {expo}')
# When formating decimals us :.[num]f to specify number of decimal places
print(f'this division will us 2 decimal places {div:.2f}')

'''
Scientific Notation
You can tell the computer to display the number in scientific notation, or "exponent" notation by using :.3e after your variable, 
where 3 defines the precision and e indicates that you are using exponent notation.

The following shows this in action:
'''
distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f"The distance is: {distance:.3e} meters.")
# Output: The distance is: 1.952e+05 meters.

# Scientific notation with 6 digits of precision
print(f"The distance is: {distance:.6e} meters.")
# Output: The distance is: 1.952100e+05 meters.

# Convert numbers from inputs directly to int or float by encasing it in the number function
con = int(input('Asking for a number please: '))
con_2 = float(input('Input a number please: '))

'''
In any case, when you want to display large numbers to the user, 
you may want to display it with commas or underscores. This is 
done by using either :, or :_ after the variable name.

The following shows this in action:
'''
big_number = 123456789

# Display without formatting:
print(f"The number is: {big_number}")
# Output: The number is: 123456789

# Display with "," formatting:
print(f"The number is: {big_number:,}")
# Output: The number is: 123,456,789

# Display with "_" formatting:
print(f"The number is: {big_number:_}")
# Output: The number is: 123_456_789