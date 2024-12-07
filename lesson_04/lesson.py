# In Python we don't need to state the type of variable
age = 32 # int
weight = 75.2 # float
name = "John" # string
is_student = True # boolean

# But it's a good practice to use the Type Hint feature
# Example - variable: type = value
age: int = 32
weight: float = 72.5
name: str = "John"
is_student: bool = True

# Usings Lists
item: str = "shoe"
item_2: str = "dress"
item_3: str = "shirt"

products: list = []

# append to add values in the list
products.append(item)
products.append(item_2)
products.append(item_3)

print(products)

# pop or remove to remove values from the list
products.pop()
products.remove(item)

print(products)

# Using Dictionaries
item_01: dict = {
  "name": "dress", 
  "price": 75.5, 
  "quantity": 30,
  "in_stock": True
}

item_02: dict = {
  "name": "shirt", 
  "price": 49.9, 
  "quantity": 0,
  "in_stock": False
}

# We can combine Lists and Dictionaries
checkout: list = []

checkout.append(item_01)
checkout.append(item_02)

print(checkout)