# Тема 3. Тема 4. Функции и стандартные модули/библиотеки
Отчёт по Теме 4 выполнил:
- Заспанов Константин Андреевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |   +         |           |
|  Задание 2  |   +         |           |
|  Задание 3  |   +         |           |
|  Задание 4  |   +         |           |
|  Задание 5  |   +         |           |
|  Задание 6  |   +         |            |
|  Задание 7  |   +         |            |
|  Задание 8  |   +         |            |
|  Задание 9  |   +         |            |
| Задание 10  |   +         |            |

# Лабораторные работа 1
## Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    print(2+5)

if __name__ == '__main__':
    main()
```

### Результат
<img width="751" height="292" alt="image" src="https://github.com/user-attachments/assets/66f0cb1e-b73d-48ff-bea0-69b12c6d60e3" />



# Лабораторные работа 2
## Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    return 2+8

if __name__ == '__main__':
    print(main())
```

### Результат
<img width="758" height="294" alt="image" src="https://github.com/user-attachments/assets/94eb677b-f0e9-44da-b461-016e9fa15518" />



# Лабораторные работа 3
## Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле.

```python
def main(mellow, melon):
    result = mellow + melon
    return result

for i in range(5):
    x = 1
    y = 10
    onsa = main(x, y)
    print(onsa)
```
### Результат
<img width="743" height="362" alt="image" src="https://github.com/user-attachments/assets/0bd72ccd-064e-435b-a9e9-70b3f029566b" />



# Лабораторные работа 4
## Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”.

```python
def main(mellow, *melon):
    red = mellow
    yellow = sum(melon)
    green = float(len(melon))
    print(f"one={red}\ntwo={yellow}\nthree={green}")

    return mellow + sum(melon) / float(len(melon))


if __name__ == "__main__":
    result = main(15, 17, 2, -2, -11, 4, -21, 17, 2)
    print(f"\nresult={result}")
```

### Результат
<img width="868" height="453" alt="image" src="https://github.com/user-attachments/assets/73d2596e-56ee-47d3-8210-007bdc98e865" />



# Лабораторные работа 5
## Напишите функцию, которая на вход получает кортеж “**kwargs” и при помощи цикла выводит значения, поступившие в функцию. На скриншоте ниже указаны два варианта вызова функции с “**kwargs” и два варианта работы с данными, поступившими в эту функцию. Комментарии в коде и теоретическая часть помогут вам разобраться в этом нелегком аспекте. Вызовите функцию используя “точку входа”.

```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")


if __name__ == "__main__":
    main(x=[1,2,3], y=[3,3,0], z=[2,3,0], q=[3,3,0], w=[3,3,0])
    print()
    main(**{'x': [1,2,3], 'y': [3,3,0]})
```

### Результат
<img width="978" height="688" alt="image" src="https://github.com/user-attachments/assets/3fa2cf30-db5a-4599-a1ed-d0abfdafa169" />



# Лабораторные работа 6
## Напишите две функции. Первая – получает в виде параметра “**kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента.
```python
def main(**kwargs):

    for i,j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == "__main__":
    main(x=[1,2,3], y=[3,4,5], z=[6,7,8], w=[9,10,11])
```
### Результат
<img width="974" height="256" alt="image" src="https://github.com/user-attachments/assets/5c8f5f22-67d5-41cc-8c66-e767926c01ff" />



# Лабораторные работа 7
## Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.

```python
from Sam4_1 import say
if __name__ == '__main__':
    say()
```
```python
def say():
    print('Miyabi likes melon')
```
### Результат
<img width="958" height="256" alt="image" src="https://github.com/user-attachments/assets/a418869d-ece6-42b4-878a-7db786e6ede1" />



# Лабораторные работа 8
## Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.

```python
import math

def main():
    melon = int(input('Введите значение: '))
    print(math.sqrt(melon))
    print(math.sin(melon))
    print(math.cos(melon))

if __name__ == '__main__':
    main()
```

### Результат
<img width="863" height="259" alt="image" src="https://github.com/user-attachments/assets/69012d13-c7c5-4264-9261-8c727609ddd4" />



# Лабораторные работа 9
## Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь.

```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели {dt.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}. "
    )

if __name__ == "__main__":
    main()
```
### Результат
<img width="855" height="279" alt="image" src="https://github.com/user-attachments/assets/346d6240-6890-47b7-903c-c962a233d68e" />



# Лабораторные работа 10
## Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.

```python
global result
def pryamoygolnik():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def treygolnik():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
    pryamoygolnik()
elif figure == '2':
    treygolnik()
print(f"Площадь: {result}")
```
### Результат
<img width="857" height="272" alt="image" src="https://github.com/user-attachments/assets/a7552850-7bea-4a7a-8728-d8cd74eaec6a" />




# Самостоятельная работа 1
## 

```python

```
### Результат



## Вывод


# Самостоятельная работа 2
## 

```python

```
### Результат



## Вывод


# Самостоятельная работа 3
##

```python

```
### Результат



## Вывод


# Самостоятельная работа 4
##

```python

```
### Результат


## Вывод


# Самостоятельная работа 5
## 

```python

```
### Результат


## Вывод


# Общий вывод

