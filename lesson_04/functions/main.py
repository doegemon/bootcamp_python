# Importing the custom function from the utils.py file
from utils import lower_name, sort_values

# Using the lower_name function
names_list: list = [" Alice ", "BOB", "Jack", "SaRaH"]
lower_names: list = [lower_name(name) for name in names_list]
print(lower_names)

# Using the sort_values function
n_list: list = [17, 58, 3, 89, 10, -32, -39, 102]
sorted_list: list = sort_values(number_list = n_list)
print(sorted_list)