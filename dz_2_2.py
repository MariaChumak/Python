def get_sign(x):
    if x[0] in '+-':
        return x[0]

lst_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(lst_1):
    sign = get_sign(lst_1[i])
    if lst_1[i].isdigit() or (sign and lst_1[i][1:].isdigit()):
        if sign:
            lst_1[i] = sign + lst_1[i][1:].zfill(2)
        else:
            lst_1[i] = lst_1[i].zfill(2)

        lst_1.insert(i, '"')
        lst_1.insert(i + 2, '"')
        i += 2
    i += 1
print(lst_1)
lst_2 = ' '.join(lst_1)
print(lst_2)