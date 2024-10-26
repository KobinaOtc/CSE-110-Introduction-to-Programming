'''
Author: Brother Otchere
Purpose: Data analysis
'''
# Declared variables
overall_max_age = None
overall_max_country = ''
overall_max_year = None
overall_min_age = None
overall_min_country = ''
overall_min_year = None
age = None
country = ''
year = None

# User input working variables
user_year = input('\nEnter the year of interest: ')
user_year_ages = []
user_year_ages_sum = 0
user_year_ages_average = None
user_max_age = None
user_max_country = ''
user_min_age = None
user_min_country = ''

# Stretch Challenge # Variable for holding the year to compare
life_expectancies = []
entity = ''
entity_year = ''
entity_life_exp = None
next_line = None
next_entity = ''
next_entity_year = ''
next_entity_life_exp = None
life_diff = None
max_life_diff = None
max_life_diff_entity = ''
first_year = ''
second_year = ''

# Stretch Challenge ask user for country # Variables below
user_country = None
user_country_life_exp = []
user_country_max_life_exp = None
user_country_max_life_exp_year = ''
user_country_min_life_exp = None
user_country_min_life_exp_year = ''
user_country_average = None
user_country_total = 0

# Print all the values in the file to test if all the value work the way I expect it to
with open('life-expectancy.csv') as life_expectancy:
    for era in life_expectancy:
        era = era.strip()
        era = era.split(',')
        life_expectancies.append(era) # Stretch Challenges append data into new list
        # Gerneral Iterations
        if era[3] == 'Life expectancy (years)':
            None
        else:
            age = float(era[3])
            country = era[0]
            year = era[2]
            if overall_max_age == None or overall_max_age < age:
                overall_max_age = age
                overall_max_country = country
                overall_max_year = year
            elif overall_min_age == None or overall_min_age > age:
                overall_min_age = age
                overall_min_country = country
                overall_min_year = year

            # User input iterations
            if year == user_year:
                user_year_ages.append(age)
                user_year_ages_sum += age
                if user_max_age == None or user_max_age < age:
                    user_max_age = age
                    user_max_country = country
                elif user_min_age == None or user_min_age > age:
                    user_min_age = age
                    user_min_country = country
            
    
# Finding average
user_year_ages_average = user_year_ages_sum / len(user_year_ages)

# Stretch Challenge identify the year and country with largest drop
for i in range(len(life_expectancies)):
    line = life_expectancies[i]
    if line[3] == 'Life expectancy (years)':
        None
    else:
        entity = line[0]
        entity_year = line[2]
        entity_life_exp = float(line[3])
        if i == len(life_expectancies) - 1:
            None
        else:
            next_line = life_expectancies[i + 1]
            next_entity = next_line[0]
            next_entity_year = next_line[2]
            next_entity_life_exp = float(next_line[3])
            if entity == next_entity:
                life_diff = entity_life_exp - next_entity_life_exp
                if max_life_diff == None:
                    max_life_diff = life_diff
                elif max_life_diff < life_diff:
                    max_life_diff = life_diff
                    max_life_diff_entity = entity
                    first_year = entity_year
                    second_year = next_entity_year





print(f'\nThe overall max life expectancy is: {overall_max_age:.2f} from {overall_max_country} in {overall_max_year}\nThe overall min life expectancy is: {overall_min_age:.2f} from {overall_min_country} in {overall_min_year}\n')
print(f'For the year {user_year}:\nThe average life expectancy across all countries was {user_year_ages_average:.2f}\nThe max life expectancy was in {user_max_country} with {user_max_age:.2f}\nThe min life expectancy was in {user_min_country} with {user_min_age:.2f}\n')
# Stretch challenge print values
print(f'The sharpest decline in life expectancies is {max_life_diff:.2f} years in {max_life_diff_entity} from {first_year} to {second_year}\n')

# Stretch Challenge ask user for country # Variables below
user_country = input('\nEnter the country of interest: ')
user_country = user_country.strip()
found = False

for i in range(len(life_expectancies)):
    line = life_expectancies[i]
    country = line[0]
    country = country.strip()

    if user_country.lower() == country.lower():
        found = True
    
    if found :
        # if line[3] == 'Life expectancy (years)':
        #     None
        # else:
        age = float(line[3])
        year = line[2]
        if user_country.lower() == country.lower():
            user_country_life_exp.append(age)
            user_country_total += age
            if user_country_max_life_exp == None or user_country_max_life_exp < age:
                user_country_max_life_exp = age
                user_country_max_life_exp_year = year
            
            if user_country_min_life_exp == None or user_country_min_life_exp > age:
                user_country_min_life_exp = age
                user_country_min_life_exp_year = year

user_country_average = user_country_total / len(user_country_life_exp)

print(f'\nFor the country {user_country.capitalize()}:\nThe average life expectancy across all years was {user_country_average:.2f}\nThe max life expectancy was in {user_country_max_life_exp_year} with {user_country_max_life_exp:.2f}\nThe min life expectancy was in {user_country_min_life_exp_year} with {user_country_min_life_exp:.2f}\n')

