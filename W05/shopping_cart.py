'''
Author: Kobina Otchere
Purpose: Shopping Cart
'''

# Declare working variables below
shopping_list = []
item_price = []
price = None
item = None
action = None
item_index = None
budget = None
total = 0

print('\nWelcome to the Shopping Cart Program!')
# Create loop to ask for shopping items
while action != 6:
    print(f'\nPlease select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Budget\n6. Quit')
    action = int(input('Please enter an action: ')) # Ask user for options
    if action == 1: # option 1 action
        item = input('What item would you like to add? ')
        price = float(input(f"What is the price of '{item}'? "))
        shopping_list.append(item)
        item_price.append(price)
        print(f"'{item.capitalize()}' has been added to the cart.")
    elif action == 2: # option 2 action
        print('The contents of the shopping cart are:')
        for i in range(len(shopping_list)):
            print(f'{i + 1}. {shopping_list[i].capitalize():6} - ${item_price[i]:.2f}') # Stretch challenge - formating prices
    elif action == 3: # option 3 action
        print('The contents of the shopping cart are:')
        for i in range(len(shopping_list)):
            print(f'{i + 1}. {shopping_list[i].capitalize():6} - ${item_price[i]:.2f}') # Stretch challenge - formating prices
        
        item_index = int(input(f'\nWhich item would you like to remove? ')) - 1
        shopping_list.pop(item_index)
        item_price.pop(item_index)
        print('Item removed.\n')
    elif action == 4: # option 4 action
        for prix in item_price: # pix == price 
            total += prix
        print(f'The total price of the items in the shopping cart is ${total:.2f}\n')
        total = 0
    # Stretch Challenge
    elif action == 5:
        budget = float(input('What is your shopping budget? '))
        for prix in item_price: # pix == price 
            total += prix
        if budget > total:
            print(f'\nYour budget is ${budget:.2f}. You will have a surplus of ${budget - total:.2f} left from the budget.\n')
        elif budget == total:
            print(f'\nYour budget is ${budget:.2f}. You have used up all of your budget\n')
        elif budget < total:
            print(f'Your budget is ${budget:.2f}. You are under budget with -${total - budget:.2f}\n')
        total = 0
    # Stretch Challenge
    else:
        if action == 6:
            print('Thank you. Goodbye.\n')
        else:
            print('Input a number corresponding to one of the options above\n')
        