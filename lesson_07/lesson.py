# Creating a simple function
def value_sum(value_1: float = 0, value_2: float = 0) -> float:
    """
    Simple function that receives two values and returns the sum of them.
    """
    return value_1 + value_2

n1 = 3
n2 = 8
n3 = 7
n4 = 2

print(value_sum())
print(value_sum(n1, n2))
print(value_sum(value_1=n1, value_2=n4))
print(value_sum(n3, n4))