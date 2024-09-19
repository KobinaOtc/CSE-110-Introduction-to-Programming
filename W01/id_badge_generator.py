# Request personal information
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_num = input('ID Number: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
month_started = input('Month Started: ')
advanced_training = input('Advanced training complete Yes/No: ')

# Print the ID Badge

print('\n----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID: {id_num}\n\n{email.lower()}\n{phone_number}\n')
# Alternatives
# print(f"Hair: {hair_color:15} Eyes: {eye_color}")
# print(f"Month: {month_started:14} Training: {advanced_training}")
print('Hair: {0:20}Eye: {1}'.format(hair_color.capitalize(), eye_color.capitalize()))
print('Month: {0:19}Training: {1}'.format(month_started.capitalize(), advanced_training.capitalize()))
print('----------------------------------------\n')