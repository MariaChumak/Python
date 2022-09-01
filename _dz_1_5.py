import math
Ax = int(input("Введите координаты точки Ax: "))
Ay = int(input("Введите координаты точки Ay: "))
Bx = int(input("Введите координаты точки Bx: "))
By = int(input("Введите координаты точки By: "))
distance = round(math.sqrt((Ax - Bx)**2 + (Ay - By)**2), 2)
print(distance)