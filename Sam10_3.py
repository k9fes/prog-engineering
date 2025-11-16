def sum():
    try:
        num = float(input("Введите число: "))
        result = 2 + num
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

sum()
sum()