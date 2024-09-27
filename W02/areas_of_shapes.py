'''
Team Activity - Areas of Shapes
'''
import math

# Prompt for square side
squ_side = float(input('\nWhat is the length of a side of the square? '))
# Calculate the area of the square --> A = L^2
squ_area = squ_side ** 2
print(f'The area of the square is: {squ_area}')

# Prompt for Rectangle sides
rec_length = float(input('What is the length of rectangle? '))
rec_width = float(input('What is the width of the rectangle? '))
# Calculate the are of the rectangle
rec_area = rec_length * rec_width
print(f'The area of the rectangle is: {rec_area}')

# Prompt for circle radius
cir_radius = float(input('What is the radius of the circle? '))
# Calculate circle area
pi = 3.14
cir_area = pi * (cir_radius ** 2)
print(f'The area of the circle is: {cir_area:.2f}')

# Stretch 
math_pi = math.pi