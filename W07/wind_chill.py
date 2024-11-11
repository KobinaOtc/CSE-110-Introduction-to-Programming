'''
Author: Brother Otchere
Purpose: Wind Chill
'''

# Declare all variables here

temp = float(input('What is the temperature? '))
temp_type = input('Fahrenheit or Celsius (F/C)? ')

speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Fuction for Wind chill t = temperature v = wind speed
def wind_chill(t, v):
    for i in range(len(v)):
        v[i] = float(v[i])
        windchill = 35.74 + (0.6215 * t) - (35.75 * (v[i] ** 0.16)) + 0.4275 * t * (v[i] ** 0.16)
        print(f'At temperature {t:.1f}F, and wind speed {int(v[i])} mph, the windchill is: {windchill:.2f}F')

# Fuction for Celsius
def celsius(tem):
    tem = (tem * (9/5)) + 32
    return tem

 
# Check for user options whether C/F
if temp_type.lower() == 'c':
    temp = celsius(temp)
    wind_chill(t=temp, v=speed)
else:
    if temp_type.lower() == 'f':
        wind_chill(t=temp, v=speed)
    else:
        print('Wrong temp type') # For creativity


