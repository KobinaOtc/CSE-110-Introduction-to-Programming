'''
Name: Brother Otchere

Project 02: Meal Price Calculator
'''

# Prompt for meal prices
child_price = float(input("\nWhat is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_child = float(input('How many children are there? '))
num_adult = float(input('How many adults are there? '))

# Creativity Task:
# For showing ceativity I will be adding drinks, appetizers, desert, 
# tip percentage and an optional percentage
# Prompt for drinks
child_drinks = float(input("\nWhat is the price of a child's drinks? "))
child_drinks_num = float(input("How many child drinks were purchased? "))
adult_drinks = float(input("What is the price of an adult's drinks? "))
adult_drinks_num = float(input("How many adult drinks were purchased? "))
# Prompt for appetizers
appetizers_price = float(input("\nWhat is the price of an appetizers? "))
appetizers_num = float(input("How many appetizers were purchased? "))
# Prompt for desert
desert_price = float(input("\nWhat is the price of a desert? "))
desert_num = float(input("How many deserts were purchased? "))


# Calculate subtotal                                               |# Creativity section added to subtotal
subtotal = (child_price * num_child) + (adult_price * num_adult) + (child_drinks * child_drinks_num) + (adult_drinks * adult_drinks_num) + (appetizers_num * appetizers_price) + (desert_num * desert_price)
print(f'\nSubtotal: ${subtotal:.2f}')

# Prompt for sales tax and total calculation
tax_rate = float(input('\nWhat is the sales tax rate? '))

# Creativitiy task:
# Promt for tips
tip_rate = float(input('\nWhat is the tip tax rate? '))
tip = subtotal * (tip_rate / 100)

# Sales tax calculation
sales_tax = subtotal * (tax_rate / 100)
total = subtotal + sales_tax + tip
# Print the results
print(f'Sales Tax: ${sales_tax:.2f}\nTip: ${tip:.2f}\nTotal: ${total:.2f}')

# Prompt for payment amount and chang calculation
payment = float(input('\nWhat is the payment amount? '))
change = payment - total

# Creativitiy task:
# Prompt to donate change to a cause
donation = input(f'Would you like to donate your change of ${change:.2f} to charity? send 1 or 2 \n1. YES\n2. NO\nReply -> ')

if donation == '1' or donation.lower() == 'yes':
    print(f'Thank you for your donation of ${change:.2f}.\n')
else:
    print(f'Change: ${change:.2f}\n')

