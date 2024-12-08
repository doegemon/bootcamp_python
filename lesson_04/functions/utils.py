# Usually the utils.py file compiles a bunch of custom functions that can be re-used in other files
# Creating a function to lower a name
def lower_name(name: str) -> str:
  return name.strip().lower()

# Creating a function to sort values from a list
def sort_values(number_list: list) -> list:
  copy_list = number_list.copy()

  for i in range(len(copy_list)):
    for j in range(i + 1, len(copy_list)):
      if copy_list[i] > copy_list[j]:
        copy_list[i], copy_list[j] = copy_list[j], copy_list[i]

  return copy_list