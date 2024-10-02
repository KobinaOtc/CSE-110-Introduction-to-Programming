'''
Author: Group 01 CSE 110 Thursday 8am MT
Purpose: Grade Calculator Program
'''

# Grade stored below
grade = ''

# Ask user for the grade percentage
grade_percentage = int(input('\nWhat is your grade percentage 0 - 100? '))

if grade_percentage >= 90:
    grade = 'A'
elif grade_percentage >= 80:
    grade = 'B'
elif grade_percentage >= 70:
    grade = 'C'
elif grade_percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'\nYour grade is: {grade}.\n')

if grade in('A', 'B', 'C'):
    print('Congratulations! You have passed the test\n')
else:
    print('Unfortunately, you need at least a "C" to pass the test. Retake the test again once you understand the topic better.\n')
