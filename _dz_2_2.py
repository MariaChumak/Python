N = 4
lst = [1]
for i in range(2, 5):
    lst.append(lst[-1] * i)
print(lst)