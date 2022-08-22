def plural_persent(n):
    persent = ['процент', 'процента', 'процентов']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2
    return str(n) + ' ' + persent[p]

print(plural_persent(1))
print(plural_persent(2))
print(plural_persent(5))