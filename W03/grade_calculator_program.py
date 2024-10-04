'''
Author: Group 01 CSE 110 Thursday 8am MT
Purpose: Grade Calculator Program
'''

# Grade stored below
grade = ''

# Ask user for the grade percentage
grade_percentage = int(input('\nWhat is your grade percentage 0 - 100? '))
grade_percentage_str = str(grade_percentage)
if grade_percentage >= 90:
    grade = 'A'
    # # Stretch Challenge
    # if grade_percentage <= 93:
    #     grade = grade + '-'
    # # Stretch Challenge
elif grade_percentage >= 80:
    grade = 'B'
    # # Stretch Challenge
    # if grade_percentage >= 87:
    #     grade = grade + '+'
    # elif grade_percentage <= 83:
    #     grade = grade + '-'
    # # Stretch Challenge
elif grade_percentage >= 70:
    grade = 'C'
    # # Stretch Challenge
    # if grade_percentage >= 77:
    #     grade = grade + '+'
    # elif grade_percentage <= 73:
    #     grade = grade + '-'
    # # Stretch Challenge
elif grade_percentage >= 60:
    grade = 'D'
    # # Stretch Challenge
    # if grade_percentage >= 67:
    #     grade = grade + '+'
    # elif grade_percentage <= 63:
    #     grade = grade + '-'
    # # Stretch Challenge
else:
    grade = 'F'

# # Stretch Challenge
# if grade_percentage >= 94 or grade_percentage < 60:
#     grade = grade
# elif int(grade_percentage_str[1]) >= 7:
#     grade += '+'
# elif int(grade_percentage_str[1]) <= 3:
#     grade += '-'
# # Stretch Challenge

## Group Stretch challenge
if grade_percentage >= 94 or grade_percentage < 60:
    grade = grade
elif grade_percentage % 10 >= 7:
    grade = grade + '+'
elif grade_percentage % 10 <= 3:
    grade = grade + '-'

print(f'\nYour grade is: {grade}.\n')

if grade_percentage >= 70:
    print('Congratulations! You have passed the test\n')
else:
    print('Unfortunately, you need at least a "C" to pass the test. Retake the test again once you understand the topic better.\n')


# if grade in('A', 'A-', 'B', 'B+', 'B-', 'C', 'C+', 'C-'):
#     print('Congratulations! You have passed the test\n')
# else:
#     print('Unfortunately, you need at least a "C" to pass the test. Retake the test again once you understand the topic better.\n')
