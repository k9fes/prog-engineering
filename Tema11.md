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
##  

```python

```

### Результат


### Вывод

# Самостоятельная работа 2
## 

```python

```

### Результат


### Вывод

## Общий вывод
