# IF EXERCISES
# I. You are analyzing a set of sales data and need to ensure that all records have positive values for quantity and price. 
# Write a program that checks these fields and prints “Valid data” if both are positive or “Invalid data” otherwise.
quantity = 10
price = 10

if quantity >= 0 and price >= 0:
  print("Valid data!")
else:
  print("Invalid data!")

# II. Imagine you are working with data from IoT sensors. 
# The data includes temperature measurements. 
# You need to classify each reading as 'Low', 'Normal' or 'High'. Whereas:
# > Temperature < 18°C is 'Low'
# > Temperature >= 18°C and <= 26°C is 'Normal'
# > Temperature > 26°C is 'High'
temperature = 29
if temperature < 18:
  print("Low temperature.")
elif temperature > 26:
  print("High temperature.")
else:
  print("Normal temperature.")

# III. Before processing user data in a recommendation system, you need to ensure that each user is aged between 18 and 65 and has provided a valid email address. 
# Write a program that validates these conditions and prints “Valid user data” or the specific error encountered.
user_age = 22
user_email = "user@email.com"

if user_age < 18 or user_age > 65:
  print('Invalid user age.')
elif "@" not in user_email or "." not in user_email:
  print("Invalid user e-mail.")
else:
  print("Valid user data.")

# IV. You are analyzing logs from an application and need to filter out messages with severity 'ERROR'. 
# Given a log record in dictionary format such as log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'}, 
# write a program that prints the message if the severity is 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'}

if log['level'] == 'ERROR':
  print(f"An ERROR happened, here is the message: {log["message"]}.")
else:
  print("No ERROR message.")

# V. You are working on a fraud detection system and need to identify suspicious transactions. 
# A transaction is considered suspicious if the amount is more than R$10,000 and if it takes place outside of business hours (before 9am or after 6pm). 
# Given a transaction such as transaction = {'amount': 12000, 'time': 20}, check whether it is suspicious.
transaction = {'amount': 12000, 'time': 29}

if transaction['amount'] > 10000 and (transaction['time'] < 9 or transaction['time'] > 18):
  print('Suspicious transaction.')
else: 
  print('Normal transaction.')

# FOR EXERCISES
# I. Given a text, count how many times each single word appears in it.
text = "I have to go to work tomorrow"
words = text.split()
word_count = {}

for word in words: 
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)

# II. Given a list of dictionaries representing user data, filter out those that have a specific field missing.
users = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

valid_users = [user for user in users if user["email"]]
print(valid_users)

# III. Given a set of sales records, calculate the total sales by category.
sales = [
    {"category": "electronics", "amount": 1200},
    {"category": "books", "amount": 200},
    {"category": "electronics", "amount": 800},
    {"category": "books", "amount": 350}
]

category_total = {}
for sale in sales: 
  category = sale['category']
  amount = sale['amount']

  if category in category_total:
    category_total[category] += amount
  else:
    category_total[category] = amount

print(category_total)

# WHILE EXERCISES
# I. Read input data until a specific keyword (“exit”) is typed.
data = []
user_input = ""
while user_input.lower() != "exit":
  user_input = str(input("Type a word or 'exit' to exit: "))
  if user_input.lower() == 'exit':
    exit()

# II. Prompt the user for a number within a specific range until the entry is valid.
n = int(input("Type a number between 1 and 10: "))
while n < 1 or n > 10:
  print("Number outside the range allowed.")
  n = int(input("Type a number between 1 and 10: "))

print("Valid number!")

# III. Simulate the consumption of a paged API, where each “page” of data is processed in a loop until there are no more pages.
actual_page = 1
last_page = 10

while actual_page <= last_page:
  print(f"Processing page {actual_page} out of {last_page} pages.")
  actual_page += 1

print("All pages have been processed.")