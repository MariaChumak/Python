x = int(input('Введите x: '))
y = int(input('Введите y: '))
if x>0 and y>0:
    print(f'{x}; {y} -> "I"')
elif x<0 and y>0:
    print(f'{x}; {y} -> "II"')
elif x<0 and y<0:
    print(f'{x}; {y} -> "III"')
elif x>0 and y<0:
    print(f'{x}; {y} -> "IV"')
elif x == 0 or y == 0:
    print(f'{x}; {y} -> "None"')