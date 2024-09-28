import math
import numpy as np
from matplotlib import pyplot as plt

result_list = []

def condition(n):

    if n == 1:
        result_list.append(n)
        return
    if n % 2 == 0:
        n = n // 2
        result_list.append(n)
        condition(n)
    else:
        n = n * 3 + 1
        result_list.append(n)
        condition(n)


initial_num = 39
condition(initial_num)
print(result_list)

plt.figure()
plt.plot(result_list, marker='o', linestyle='-', color='r')
plt.title(f'Collatz Sequence starting from {initial_num}')
plt.xlabel('Step')
plt.ylabel('Value')
plt.grid(True)
plt.show()
