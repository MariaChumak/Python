def sum_nums(value):
    res = 0
    while value != 0:
        res += value % 10
        value // 10
        return res
lst_1 = [num ** 3 for num in range(1, 1001) if num % 2 == 1]
lst_2 = sum(filter(lambda num: sum_nums(num) % 7 == 0, lst_1))
lst_3 = sum(filter(lambda num: sum_nums(num + 17) % 7 == 0, lst_1))
print(lst_1)
print(lst_2)
print(lst_3)