# The challenge is to re-factor the code from the exercise of the 3rd lesson, using Type Hint and Dictionaries
valid_name: bool = False
valid_salary: bool = False
valid_bonus: bool = False
stop: bool = False
bonus_list: list = []

# I. Ask the user to type employee's name
while stop == False: 
  employee_dict: dict = {}

  while valid_name == False:
    try:
      name: str = str(input("Enter the employee's name: "))

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

  # II. Ask the user to type the employee's salary
  while valid_salary == False:
    try: 
      salary: int = int(input("Enter employee's monthly salary: "))
      slry_float: float = float(salary)

      if slry_float <= 0:
        print("The salary can't be negative or equal to zero.")
      else:
        print("Valid salary.")
        valid_salary = True
    except ValueError:
      print("Invalid salary, please use numbers only.")

  # III. Ask the user to type the bonus factor
  while valid_bonus == False:
    try:
      factor: float = float(input('Enter the bonus factor: '))

      if factor <= 0:
        print("The bonus factor can't be negative or equal to zero.")
      else:
        print("Valid bonus factor.")
        valid_bonus = True
    except ValueError:
      print("Invalid bonus factor, please use numbers only.")

  # IV. Calculate the bonus amount (1000 + salary * bonus factor)
  FIXED_VALUE: int = 1000
  bonus: float = FIXED_VALUE + slry_float * factor

  employee_dict["Employee Name"] = name
  employee_dict["Monthly Bonus Amount"] = bonus

  bonus_list.append(employee_dict)

  user_stop: str = str(input('Want to add another worker? (Y/N): '))

  if user_stop == "Y":
    valid_name = False
    valid_salary = False
    valid_bonus = False
  else:
    print("Here's the list of employees registered and their bonus amount:")
    print(bonus_list)
    stop = True