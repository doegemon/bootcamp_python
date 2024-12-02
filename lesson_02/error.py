# Trying to divide a number by zero
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
division = n1 / n2

print(f'{n1} divided by {n2} is equal to {division}')

# The error ZeroDivisionError: division by zero pops up
# We can use try + except to deal with errors
try:
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    division = n1 / n2

    print(f'{n1} divided by {n2} is equal to {division}')
# Show a specific message/do something specific depending on the type of error
except ZeroDivisionError as z: 
    print(z)
    print("It's not possible to divide a number by zero!")
except ValueError as v:
    print(v) 
    print('Please enter a number.')
except: 
    print('Something went wrong, please try again.')
# Show a specific message/do something specific if everything went smoothly
else: 
    print('Thanks for using the program!')
# Show a specific message/do something specific regardless the outcome (success or error)
finally: 
    print('Division Software by Division Inc.')

# Also, we can use isinstance() to check the type of a variable
# n1 = "foo"
n1 = 10
if isinstance(n1, int):
  print(f'Your number is: {n1}')
else:
  print('Please enter a number.')