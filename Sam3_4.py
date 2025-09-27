melon = input("Введите предложение: ")

print("Длина предложения:", len(melon))
print("В нижнем регистре:", melon.lower())

vowels = sum(1 for char in melon.lower() if char in 'aeiou')
print("Количество гласных:", vowels)

new_melon = melon.replace("ugly", "beauty")
print("После замены 'ugly' на 'beauty':", new_melon)

print("Начинается с 'The':", melon.startswith("The"))
print("Заканчивается на 'end':", melon.endswith("end"))
