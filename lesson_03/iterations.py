import time
# I. Using if + elif + else to check conditions
n = int(input("Enter a number: "))

if n < 0: 
  print(f"The number {n} is a negative number.")
elif n == 0: 
  print("Your number is 0.")
elif n == 1:
  print("Your number is 1.")
else:
  print(f"Your number {n} is a positive number")

# II. Using FOR to go through all items in a sequence
names = ["Mary", "John", "David", "Mark", "Travis"]

print("Printing Names in the names list:")
for name in names: 
  print(name)
  print("==--==")

# III. Using WHILE to go through all items in a unknown sequence - it will keep executing until a condition is no longer fulfilled
condition = True

while condition: 
  print("Checking data and executing ETL..")
  time.sleep(10)