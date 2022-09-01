import math
n = 6
lst = [(1 + 1 / i) ** i for i in range(1, 7)]
total = sum(lst)
print(round(total, 3))