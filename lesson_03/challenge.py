# The challenge is to re-factor the code from the exercise of the 2nd lesson, using While to prompt the user to enter the correct information
valid_name = False
valid_salary = False
valid_bonus = False

# I. Ask the user to type their name
while valid_name == False:
  try:
    name = str(input('Enter your name: '))

    if len(name) == 0: 
      raise ValueError("You have to type a name")
    elif any(char.isdigit() for char in name): 
      raise ValueError("The name can't have numbers in it.")
    elif name.isspace():
      raise ValueError("The name can't be empty.")
    else: 
      print("Valid name.")
      valid_name = True
  except ValueError as e:
    print(e)

# II. Ask the user to type their salary and convert it to float
while valid_salary == False:
  try: 
    salary = int(input('Enter your monthly salary: '))
    slry_float = float(salary)

    if slry_float <= 0:
      print("Your salary can't be negative or equal to zero.")
    else:
      print("Valid salary.")
      valid_salary = True
  except ValueError:
    print("Invalid salary, please use numbers only.")

# III. Ask the user to type their bonus factor
while valid_bonus == False:
  try:
    factor = float(input('Enter your bonus factor: '))

    if factor <= 0:
      print("Your bonus factor can't be negative or equal to zero.")
    else:
      print("Valid bonus factor.")
      valid_bonus = True
  except ValueError:
    print("Invalid bonus factor, please use numbers only.")

# IV. Calculate the bonus amount (1000 + salary * bonus factor)
FIXED_VALUE = 1000
bonus = FIXED_VALUE + slry_float * factor

# V. Print the result for the user
print(f'Hello {name}! Your bonus is equal to {bonus}.')