from Sam4_5_1 import heron

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
melon = heron(a, b, c)
print("Площадь треугольника:", melon)