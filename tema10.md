# Тема 10. Декораторы и исключения
Отчёт по Теме 10 выполнил:
- Заспанов Константин Андреевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |            |
|  Задание 2  |     +       |            |
|  Задание 3  |            |            |
|  Задание 4  |            |            |
|  Задание 5  |            |            |


# Лабораторные работа 1
## Вам нужно написать программу, которая будет считать числа Фибоначчи для 100 и запустить ее без этого декоратора и с ним, посмотреть на разницу во времени решения поставленной задачи. P.S. при запуске без декоратора можете долго не ждать, для наглядности хватит 10 секунд ожидания.

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(100))
```
### Результат
<img width="580" height="262" alt="image" src="https://github.com/user-attachments/assets/14c88d45-4a19-4423-9b38-d2c14930951b" />


# Лабораторные работа 2
## Напишите декоратор для функции, который будет принимать все параметры вызываемой функции (имя, возраст) и проверять чтобы возраст был больше 0 и меньше 130.

```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)
    return output_func

@check
def personal_info(name, age):
    print(f"Имя: {name} Возраст: {age}")

if __name__ == '__main__':
    personal_info('Miyabi', 25)
    personal_info('Melon', -5)
    personal_info('Watermelon', 180, 1313, -854)
```
### Результат
<img width="579" height="266" alt="image" src="https://github.com/user-attachments/assets/335a342e-c686-4fc0-ab3c-e466680bdd3e" />


# Лабораторные работа 3
## Воспользуйтесь исключениями, чтобы неподходящий тип данных не ломал ваш сайт. Также дополнительно можете обернуть весь код функции в try/except/finally для того, чтобы программа вас оповестила о том, что выявлена какая-то ошибка или программа успешно выполнена.

```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i]*15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информаия обработана')

if __name__ == '__main__':
    data([1, 15, 'Я','Пытаюсь','сломать','твой','сайт', 89, 34])

```
### Результат
<img width="587" height="448" alt="image" src="https://github.com/user-attachments/assets/5c60f87e-b279-4d53-b47f-2a132ca32eed" />


# Лабораторные работа 4
## Продолжая работу над сайтом, вы решили написать собственное исключение, которое будет вызываться в случае, если в функцию проверки имени при регистрации передана строка длиннее десяти символов, а если имя имеет допустимую длину, то в консоль выводиться “Успешная регистрация”

```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')
if __name__ == '__main__':
    name = '123456789'
    check_name(name)
```
### Результат
<img width="617" height="218" alt="image" src="https://github.com/user-attachments/assets/1ca78661-423d-4e98-bd01-29e8d95c3dee" />

# Лабораторные работа 5
## После запуска сайта вы поняли, что вам необходимо добавить логгер, для отслеживания его работы. Готовыми вариантами вы не захотели пользоваться, и поэтому решили создать очень простую пародию. Для этого создали две функции: 		init		() (вызывается при создании класса декоратора в программе) и 	call	() (вызывается при вызове декоратора). Создайте необходимый вам декоратор. Выведите все логи в консоль.

```python
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func
    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```
### Результат
<img width="627" height="344" alt="image" src="https://github.com/user-attachments/assets/a849b49e-5eeb-4fe5-8f04-1af824e80478" />

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


# Самостоятельная работа 3
## 

```python

```

### Результат


### Вывод

# Самостоятельная работа 4
## 

```python

```

### Результат


### Вывод

# Самостоятельная работа 5
## 

```python

```

### Результат


### Вывод

# Общий вывод
