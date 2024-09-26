# Prompt user to for age
age = int(input('\nHow old are you? '))
# next age = age + 1
nxt_age = age + 1
print(f'On your next birthday, you will be {nxt_age}\n')

# Prompt for number of egg cartons
egg_cart = int(input('How many egg cartons do you have? '))
# For total of the eggs multiply by 12
total_eggs = egg_cart * 12
print(f'You have {total_eggs} eggs\n')

# Prompt for number of coockies available
coockies = float(input('How many cookies do you have? '))
# Prompt for number of people sharing
eaters = float(input('How many people are there? '))
# Divide number of cookies by eaters
cookie_per_eater = coockies/eaters
print(f'Each person may have {cookie_per_eater} cookies\n')
