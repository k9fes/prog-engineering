import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_1 = sorted(one)[:1]
min_2 = sorted(two)[:1]
min_3 = sorted(three)[:1]
max_1 = sorted(one)[-1:]
max_2 = sorted(two)[-1:]
max_3 = sorted(three)[-1:]
min = min_1 + min_2 + min_3
max = max_1 + max_2 + max_3

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

area_min = triangle_area(*min)
area_max = triangle_area(*max)

print(f" Площадь из минимальных сторон: {area_min:.2f}")
print(f" Площадь из максимальных сторон: {area_max:.2f}")