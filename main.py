import math
import numpy as np

result_list = []
def condition(n):
    if n == 1:  # Base case to terminate recursion
        result_list.append(n)
        return
    if n % 2 == 0:  # If n is even
        n = n // 2
        result_list.append(n)
        condition(n)  # Recursive call
    else:  # If n is odd
        n = n * 3 + 1
        result_list.append(n)
        condition(n)  # Recursive call

condition(6)
print(result_list)
