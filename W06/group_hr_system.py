# Variables Decleared here
name = ''
job = ''
personal_id = ''
salary = None
# Open and print all the values in the file
with open('hr_system.txt') as hr_system:
    for person in hr_system:
        person = person.strip() # Strech challenge one
        person = person.split()
        name = person[0]
        personal_id = person[1]
        job = person[2]
        salary = float(person[3])
        # Stretch Challeng two
        paycheck = salary / 24

        # Stretch Challenge three
        if job.lower() == 'engineer':
            paycheck += 1000

        # print(f'Name: {name}, Title: {job}')
        # Stretch Challenge one
        # print(f'{name} (ID: {personal_id}), {job} - ${salary:.2f}')

        # Stretch Challenge two
        print(f'{name} (ID: {personal_id}), {job} - ${paycheck:.2f}')
