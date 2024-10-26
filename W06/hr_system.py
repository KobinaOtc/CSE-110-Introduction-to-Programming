'''
Author: 01 CSE 110 Thursday 8am MT
Purpose: Human Resource System
'''
# Declare variables
personal_details = None
name = ''
job = ''
person_id = None
salary = None

# Open and print out the values in the file
with open('hr_system.txt') as hr_system:
    for person in hr_system:
        person = person.strip() # Stretch Challenge
        personal_details = person.split()
        name = personal_details[0]
        job = personal_details[2]
        person_id = personal_details[1]
        salary = float(personal_details[3])
        pay_check = salary / 24
        if job.lower() == 'engineer':
            pay_check += 1000
        print(f'{name} (ID: {person_id}), {job} - ${pay_check:.2f}')
