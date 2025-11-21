# Тема 11. Итераторы и генераторы
Отчёт по Теме 11 выполнил:
- Заспанов Константин Андреевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |            |
|  Задание 2  |     +       |            |
|  Задание 3  |     +       |            |
|  Задание 4  |     +       |            |
|  Задание 5  |     +       |            |


# Лабораторные работа 1
## Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```python
num = [0,1,2,3,4,5]
for item in num:
    print(item)
```
### Результат
<img width="535" height="343" alt="image" src="https://github.com/user-attachments/assets/b49127bd-9b5d-48c1-8b60-45cb07c35b9f" />

# Лабораторные работа 2
## Класс итератор с гибкой настройкой и удобными применением

```python
class CountDown:
    def __init__(self,start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == "__main__":
    counter = CountDown(10)
    for i in counter:
        print(i)
```
### Результат
<img width="503" height="480" alt="image" src="https://github.com/user-attachments/assets/ba64935b-c72a-4270-b9e4-f964d25efda3" />

# Лабораторные работа 3
## Генератор списка

```python
a = [i** 2 for i in range(1,5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```
### Результат
<img width="725" height="464" alt="image" src="https://github.com/user-attachments/assets/1ccfe347-d70f-4fad-8b3f-267ec85efa46" />

# Лабораторные работа 4
## Выражения генераторы
```python
b = (i** 2 for i in range(1,5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```
### Результат
<img width="617" height="390" alt="image" src="https://github.com/user-attachments/assets/91467556-c9c2-482e-8e20-a944346b0e61" />

# Лабораторные работа 5
## Такой же счетчик, как и в первом задании, только это генератор и использует yield 

```python
def countdown(count):
    while count >=0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(10)
    for i in counter:
        print(i)
```
### Результат
<img width="597" height="479" alt="image" src="https://github.com/user-attachments/assets/99b7412e-9fdb-4e5e-bef6-ad337459c6e0" />

# Самостоятельная работа 1
## Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for n in fib (300):
    print(f'{n}')
```

### Результат
<img width="665" height="458" alt="image" src="https://github.com/user-attachments/assets/e839c225-a087-4190-a7a2-9e4ae99fb1ff" />

### Вывод
Использование генератора с yield позволяет эффективно генерировать числа Фибоначчи без загрузки всей последовательности в память. Это полезно при работе с большими последовательностями, так как экономит ресурсы памяти.

# Самостоятельная работа 2
## К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 300
with open("fib.txt", "w") as file:
    for number in fib(n):
        file.write(f"{number}\n")

print("Числа Фибоначчи записаны в файл 'fib.txt'.")
```

### Результат
<img width="778" height="860" alt="image" src="https://github.com/user-attachments/assets/5d636d19-dbcd-4654-93e2-30b72555a4bd" />

### Вывод
Генератор позволяет эффективно генерировать и записывать числа без загрузки всей последовательности в память.
## Общий вывод
