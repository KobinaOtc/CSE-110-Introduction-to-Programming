# Name input requests
first_name = input('\nWhat is your first name: \n')
last_name = input('\nWhat is your last name: \n')

# Print the results
print('\nWelcome', first_name.capitalize(), last_name.capitalize(), 'to the OTchTech service portal: \nSelect from one of the options below\n1. Service Info\n2. Request quote\n3. Payment Request\n')

# Othere string edits include: lower(), upper(), count('Letter'), title(), 

# String Formating

print('Here are some of the ways you can format your name\n')
# Defining output fomats 1
output_one = 'Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize()
print("output 1 => output_one = 'Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize()")
print('Results:', output_one)
# Defining output fomats 2
output_two = 'Hello, {} {}'.format(first_name.capitalize(), last_name.capitalize())
print("\noutput 2 => output_two = 'Hello, {} {}'.format(first_name.capitalize(), last_name.capitalize())")
print('Results:', output_two)
# Defining output fomats 3
output_three = 'Hello, {1} {0}'.format(first_name.capitalize(), last_name.capitalize())
print("\noutput 3 => output_three = 'Hello, {1} {0}'.format(first_name.capitalize(), last_name.capitalize())")
print('Results:', output_three)
# Defining output fomats 4
output_four = f'Hello, {first_name.capitalize()} {last_name.capitalize()}'
print("\noutput_four = f'Hello, {first_name.capitalize()} {last_name.capitalize()}'")
print('Results:', output_four, '\n')

