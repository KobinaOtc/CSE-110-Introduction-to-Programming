'''
Python comes with many libraries built-in. One of these is called the "Math" library, 
and it contains common mathematical functions and operations. In order to use code from 
this library in your program, you'll need to import or include it. You do this by putting 
the code import math at the top of your program. For example, if you wanted to use the 
value of Pi included in the math library you do so as follows:
'''
import math

radius = 5
area = math.pi * (radius ** 2)
print(f'The area is: {area}')
# Output: The area is: 78.53981633974483

'''
math.ceil(value)—Rounds value up to the next whole number, the "ceiling."
math.floor(value)—Rounds value down to the next whole number.
math.exp(value)—Raises e to the power of value.
math.sin(value)—Computes the trigonometry sine function of value in radians.
'''
weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2
