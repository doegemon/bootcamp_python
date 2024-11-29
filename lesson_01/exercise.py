# I. Ask the user to type his/her name
name = str(input('Enter your name: '))

# II. Ask the user to type his/her salary and convert it to float
salary = int(input('Enter your monthly salary: '))
to_float = float(salary)

# III. Ask the user to type his/her bonus factor
factor = float(input('Enter your bonus factor: '))

# IV. Calculate the bonus amount (1000 + salary * bonus factor)
constant = 1000
bonus = constant + salary * factor

# V. Print the result for the user
print(f'Hello {name}! Your bonus is equal to {bonus}')