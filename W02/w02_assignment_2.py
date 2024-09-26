# Prompt for temperature in Fahrenheit
fahrenheit = float(input('\nWhat is the temperature in Fahrenheit? '))
convert_to_celcius = (fahrenheit - 32) * (5 / 9)
print(f'The temperature in Celsius is {convert_to_celcius:.1f} degrees.\n')