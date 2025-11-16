def format_output_decorator(func):
    #Декоратор для форматирования вывода функции.
    #Добавляет рамку вокруг результата и преобразует текст в верхний регистр.

    def wrapper(*args, **kwargs):
        # Декоратор не знает, какие аргументы принимает оригинальная функция,
        # поэтому используем *args и **kwargs для передачи всех параметров
        result = func(*args, **kwargs)
        # Форматируем вывод с рамкой и в верхнем регистре
        formatted_result = str(result).upper()
        # Создание декоративной рамки
        border = "=" * (len(formatted_result) + 4)
        # Вывод форматированного результата
        print(f"\n{border}")
        print(f"| {formatted_result} |")
        print(f"{border}\n")
        # Возвращаем оригинальный результат (не отформатированный)
        # чтобы не нарушать логику работы вызывающего кода
        return result
    return wrapper

@format_output_decorator
def greet(name):
    return f"Привет, {name}!"

@format_output_decorator
def volume(a, b, c):
    #Функция вычисления объёма дыны (эллипсоида)
    volume = 4/3 * 3.14 * a * b * c
    return f"Объём дыни с размерами: {a, b, c} равен {volume:.2f}"

greet("Miyabi")
volume(50, 15, 25)