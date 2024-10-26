# Declare all variables here
life_expectancy = []
entity = ''
year = ''
life_ex = None
country = ''
first_year = ''
second_year = ''

time_diff = None
max_time_diff = None

# For min life variables
min_life_ex = None
min_life_ex_country = ''
min_life_ex_year = ''

# Open and iterate through the file

with open('life-expectancy.csv') as life_exp:
    for line in life_exp:
        line = line.strip()
        line = line.split(',')
        life_expectancy.append(line)
        # line = life_expectancy
        # line = line.split(',')
        # if line[3] == 'Life expectancy (years)':
        #     None
        # else:
        #     entity = line[0]
        #     year = line[2]
        #     life_ex = float(line[3])
        #     if min_life_ex == None or min_life_ex > life_ex:
        #         min_life_ex = life_ex
        #         min_life_ex_country = entity
        #         min_life_ex_year = year
    
    # print(life_expectancy)
    # print(f'\nThe overall min life expectancy is: {min_life_ex} from {min_life_ex_country} in {min_life_ex_year}\n')

for i in range(len(life_expectancy)):
    line = life_expectancy[i]
    if line[3] == 'Life expectancy (years)':
        None
    else:   
        entity = line[0]
        year = line[2]
        life_time = float(line[3])
        next_line = None
        if i == len(life_expectancy) - 1:
            None
        else:
            next_line = life_expectancy[i + 1]
            next_entity = next_line[0]
            next_year = next_line[2]
            next_life_time = float(next_line[3])
            if entity == next_entity:
                time_diff = life_time - next_life_time
                if max_time_diff == None:
                    max_time_diff = time_diff
                elif max_time_diff < time_diff:
                    max_time_diff = time_diff
                    country = entity
                    first_year = year
                    second_year = next_year

print(f'The sharpest decline in life expectancies is {max_time_diff} years in {country} from {first_year} to {second_year}')

    # print(i)