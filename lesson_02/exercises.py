# I. Write a program that converts the temperature from Celsius to Fahrenheit. 
# The program should ask the user for the temperature in Celsius and, using try-except, ensure that the input is numeric, handling any ValueError. 
# Print the result in Fahrenheit or an error message if the input is not valid.
try:
  celsius = float(input('Enter the temperature in Celsius: '))
  to_fahren = (celsius * 1.8) + 32

  print(f'{celsius} degrees Celsius is equal to {to_fahren} degrees Fahrenheit')
except: 
  print('Please enter a valid temperature.')

# II. Create a program that checks whether a word or phrase is a palindrome (it reads equally from back to front, disregarding spaces and punctuation). 
# Use try-except to ensure that the input is a string. 
print('Palindrome Checker')
word = str(input('Please enter a word or phrase: '))
if word.isnumeric():
  print('Please enter a valid word.')
else:
  formatted = word.replace(" ", "").lower()
  reverse = formatted[::-1]
  if formatted == reverse:
    print(f"The word/phrase '{word}' is a palindrome.")
  else:
    print(f"The word/phrase '{word}' is not a palindrome.")

# III. Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. 
# Use try-except to handle divisions by zero and non-numeric inputs. 
# Use if-elif-else to perform the mathematical operation based on the operator provided. 
# Print the result or an appropriate error message.
print('Calculator Software')
try:
  n1 = float(input('Please enter the first number: '))
  n2 = float(input('Please enter the second number: '))
  op = str(input('What kind of operation? (+, -, *, /) '))

  if op == '+':
    form = n1 + n2
    print(f"{n1} plus {n2} is equal to {form}")
  elif op == '-':
    form = n1 - n2
    print(f"{n1} minus {n2} is equal to {form}")
  elif op == '*':
    form = n1 * n2
    print(f"{n1} times {n2} is equal to {form}")
  elif op == '/':
    form = n1 / n2
    print(f"{n1} divided by {n2} is equal to {form}")
  else: 
    print('Please enter a valid math operator.')
except ZeroDivisionError:
  print("Error, it's not possible to divide a number by zero.")
except:
  print("Error, please enter a valid number.")

# IV. Write a program that asks the user to enter a number. 
# Use try-except to ensure that the input is numeric and use if-elif-else to classify the number as “positive”, 
# “negative” or “zero”. Additionally, identify whether the number is “even” or “odd”.
print('Number Classificator')
try:
  n = float(input("Please enter a number: "))
  if n > 0:
    cl = 'Positive'
  elif n == 0:
    cl = 'Zero'
  else:
    cl = 'Negative'
  
  if n == 0:
    typ = 'Neutral'
  elif n % 2 == 0:
    typ = 'Even'
  else:
    typ = 'Odd'

  print(f"The number {n} is {cl} and {typ}.")
except:
  print("Error, please enter a valid number.")

# V. Create a script that asks the user for a list of comma-separated numbers. 
# The program must convert the input string into a list of integers. 
# Use try-except to handle the conversion of each number and validate that each element of the converted list is an integer. 
# If the conversion fails or an element is not an integer, print an error message. 
# If the conversion is successful for all elements, print the list of integers.
numbers = str(input("Please provide some numbers/integers separated by commas: "))
list = numbers.split(",")
new_list = []
try:
  for n in list:
    new_list.append(int(n.strip()))
  print(f'Numbers List: {new_list}')
except:
  print('Something went wrong, please try again.')