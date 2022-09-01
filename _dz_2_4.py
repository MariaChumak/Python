import random
N = int(input())
lst = [-N, N]
print(lst)
a = random.randrange(-N, N + 1)
b = random.randrange(-N, N + 1)
print(a, b)
print(a * b)