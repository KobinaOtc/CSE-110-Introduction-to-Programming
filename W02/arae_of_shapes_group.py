'''
Team Activity - Areas of Shapes
'''

# Stretch challenge 01. 
import math
# Stretch challenge 01. 

# Prompt for square side
squ_side = float(input('\nWhat is the length of a side of the square in centimeters? '))
squ_area = squ_side ** 2
# Stretch challenge 03. 
squ_area_in_meters = (squ_side / 100) ** 2
print(f'The area of the square is: {squ_area:.2f}cm square or {squ_area_in_meters:.4f}m square')
# Stretch challenge 03. 

# Prompt for Rectangle sides
rec_length = float(input('\nWhat is the length of rectangle? '))
rec_width = float(input('What is the width of rectangle? '))
# Calculate the area
rec_area = rec_length * rec_width
# Stretch challenge 03. 
rec_area_in_meters = (rec_length / 100) * (rec_width / 100)
print(f'The area of the rectangle is: {rec_area:.2f}cm square or {rec_area_in_meters:.4f}m square')
# Stretch challenge 03. 

# Prompt for Circle radius
# Stretch challenge 01.
pi = math.pi
# Stretch challenge 01. 
radius = float(input('\nWhat is the radius of the circle? '))
circ_area = (radius ** 2) * pi
# Stretch challenge 03. 
circ_area_in_meters = ((radius / 100) ** 2) * pi
print(f'The area of the circle is: {circ_area:.2f}cm square or {circ_area_in_meters:.2f}m square\n')
# Stretch challenge 03. 

# Stretch challenge 02. 
# Prompt for length for calculation
len_prompt = float(input('Give me a length: '))
# For square area
len_squ_area = len_prompt ** 2
# For Circle area
len_circ_area = (len_prompt ** 2) * pi
# For square Volume
cube_volume = len_prompt ** 3
# For sphere volume
sphere_volume = (4 / 3) * pi * (len_prompt ** 3)
print(f'The area of a square with side {len_prompt} = {len_squ_area:.2f}\nThe area of a circle with raduis {len_prompt} = {len_circ_area:.2f}')
print(f'The volume of a cube with side {len_prompt} = {cube_volume:.2f}\nThe volume of a sphere with side {len_prompt} = {sphere_volume:.2f}\n')
# Stretch challenge 02. 