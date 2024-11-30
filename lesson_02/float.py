# I. Ask the user to enter 2 floats and display the sum
n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))
sum = n1 + n2

print(f'The sum of the two numbers is: {sum}')

# II. Ask the user to enter 2 floats and display the average
n3 = float(input('Enter the first number: '))
n4 = float(input('Enter the second number: '))
avg = (n3 + n4) / 2

print(f'The average of the two numbers is: {avg}')

# III. Develop a program that calculates the power of a number (base and exponent supplied by the user)
base = float(input('Enter the base number: '))
exponent = float(input('Enter the exponent number: '))
power = base ** exponent

print(f'The result is equal to {power}')

# IV. Make a program that converts the temperature from Celsius to Fahrenheit.
celsius = float(input('Enter the temperature in Celsius: '))
to_fahren = (celsius * 1.8) + 32

print(f'{celsius} degrees Celsius is equal to {to_fahren} degrees Fahrenheit')

# V. Write a program that calculates the area of a circle, taking the radius as input.
radius = float(input('Enter the radius of the circle: '))
area = 3.14159265 * (radius ** 2)

print(f'The area of the circle is equal to: {area}')