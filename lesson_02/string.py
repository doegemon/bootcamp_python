# I. Write a program that receives a string from the user and converts it to uppercase
text = str(input('Enter a name/word: '))
to_upper = text.upper()

print(f'Uppercase = {to_upper}')

# II. Create a program that receives the user's full name and prints it with all lower-case letters.
name = str(input('Enter your full name: '))
upper_name = name.upper()

print(f'Uppercase Name = {upper_name}')

# III. Make a program that asks the user to enter a date in the format “dd/mm/yyyy” and then prints the day, month and year separately.
date = str(input('Enter a date (in the format "dd/mm/yyyy"): '))
split = date.split('/')
day = split[0]
mth = split[1]
year = split[2]

print(f'Day = {day}')
print(f'Month = {mth}')
print(f'Year = {year}')