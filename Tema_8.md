# Тема 8. Основы объектно-ориентированного программирования
Отчёт по Теме 8 выполнил:
- Заспанов Константин Андреевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |      +      |
|  Задание 2  |     +       |      +      |
|  Задание 3  |     +       |      +      |
|  Задание 4  |     +       |      +      |
|  Задание 5  |     +       |      +      |


# Лабораторные работа 1
## Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Устанавливаем атрибут производителя
        self.model = model  # Устанавливаем атрибут модели
        
# Создание экземпляра (объекта) класса Car
# Передаём значения "Toyota" для make и "Corolla" для model
my_car = Car("Toyota", "Corolla")

```

# Лабораторные работа 2
## Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Определяем класс Car
class Car:
    def __init__(self, make, model):
        # Конструктор класса
        # Атрибут производителя
        self.make = make
        # Атрибут модели
        self.model = model

    def drive(self): #Метод drive имитирует движение автомобиля.
        print(f"Автомобиль {self.make} {self.model} начинает движение!")


# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")

# Вызываем метод drive у созданного объекта
my_car.drive()
```
### Результат
<img width="770" height="208" alt="image" src="https://github.com/user-attachments/assets/336ffb4a-7f33-4bda-a87a-9c696d18f768" />

# Лабораторные работа 3
##     3) Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 

```python
# класс Car
class Car:
    # конструктор базового класса
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # метод для движения автомобиля
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# класс ElectricCar наследуется от класса Car и использует все методы и атрибуты родительского класса
class ElectricCar(Car):
    # конструктор класса ElectricCar
    # принимает дополнительный параметр battery_capacity (емкость батареи)
    def __init__(self, make, model, battery_capacity):
        # вызываем конструктор родительского класса Car
        # super() - обращение к родительскому классу
        super().__init__(make, model)
        # добавляем новый атрибут
        self.battery_capacity = battery_capacity

    # новый метод
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# создаем объект класса Car
my_car = Car("Toyota", "Corolla")
# используется метод drive
my_car.drive()
# создаем объект класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)
# используется унаследованный метод drive
my_electric_car.drive()
# используется метод charge
my_electric_car.charge()
```
### Результат
<img width="733" height="277" alt="image" src="https://github.com/user-attachments/assets/90d87b0d-4505-4591-98c4-5b8bcaaab6d9" />

# Лабораторные работа 4
## Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Класс Car с инкапсуляцией
class Car:
    # Конструктор класса
    def __init__(self, make, model):
        self._make = make # Защищенный атрибут (одно подчеркивание) условно приватный - доступен, но не рекомендуется использовать извне
        self.__model = model # Приватный атрибут (два подчеркивания) строго приватный - доступ ограничен
    # Метод для движения автомобиля использует защищенный и приватный атрибуты внутри класса
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")
# Доступ к защищенному атрибуту (работает, но не рекомендуется)
print(my_car._make)
# print(my_car.__model)  # Ошибка! Приватный атрибут не доступен
# Вызываем метод drive() - внутри класса доступны все атрибуты
my_car.drive()
```
### Результат
<img width="730" height="266" alt="image" src="https://github.com/user-attachments/assets/952ce940-8f02-42e7-a4ea-d3f510e18177" />

# Лабораторные работа 5
## Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Базовый класс Shape
class Shape:
    # Базовый метод для вычисления площади
    # В базовом классе этот метод возвращает 0 (заглушка)
    def area(self):
        return 0.0


# Класс Rectangle наследуется от Shape
class Rectangle(Shape):
    # Конструктор принимает ширину и высоту
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Переопределяем метод area для прямоугольника
    # Площадь прямоугольника = ширина * высота
    def area(self):
        return self.width * self.height


# Класс Circle наследуется от Shape
class Circle(Shape):
    # Конструктор принимает радиус
    def __init__(self, radius):
        self.radius = radius

    # Переопределяем метод area для круга
    # Площадь круга = π*r²
    def area(self):
        return 3.14 * self.radius * self.radius


# Создаем массив с фигурами
shapes = [Rectangle(50, 10), Circle(10)] # Прямоугольник 50x10 # Круг с радиусом 10

# Проходим по массиву и выводим площади фигур
# Метод area() вызывается для разных типов объектов
for shape in shapes:
    print(shape.area())
```
### Результат
<img width="838" height="241" alt="image" src="https://github.com/user-attachments/assets/1b2d84b0-8312-4e74-ba32-fc239a02ff7f" />

# Самостоятельная работа 1
## Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли. 

```python
class  Rod:

    def __init__(self, manufacturers, type):
        self.manufacturers = manufacturers
        self.type = type

my_rod = Rod("Shimano", "Feeder")

print(f"Производитель: {my_rod.manufacturers}")
print(f"Тип: {my_rod.type}")

```

### Результат
<img width="812" height="236" alt="image" src="https://github.com/user-attachments/assets/d2230f72-9b14-4d80-813c-8750c46a129e" />

### Вывод
Создан класс Rod с атрибутами: производитель и тип. 

# Самостоятельная работа 2
## Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Rod:
    def __init__(self, manufacturer, rod_type, has_reel):
        self.manufacturer = manufacturer
        self.type = rod_type
        self.has_reel = has_reel.lower()

    def display_info(self):
        print(f"Производитель: {self.manufacturer}")  # Исправлено на self
        print(f"Тип: {self.type}")

    def check_reel(self):

        if self.has_reel in ['yes', 'да', 'есть', '1', 'true']:
            print("Снасть содержит катушку")
        else:
            print("У снасти отсутствует катушка")

my_rod = Rod("Shimano", "Feeder", "yes")

my_rod.display_info()
my_rod.check_reel()
```

### Результат
<img width="890" height="265" alt="image" src="https://github.com/user-attachments/assets/4bf12ad4-fbaf-4a2f-99bb-9326d32d7836" />

### Вывод
Добавлен атрибут has_reel, а также метод check_reel.

# Самостоятельная работа 3
## Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Rod:
    def __init__(self, brand, length):
        self.brand = brand
        self.length = length

    def use(self):
        print(f"Использование удилища {self.brand} длинной  {self.length} ")

class SpinningRod(Rod):
    def __init__(self, brand, length, test_range):
        super().__init__(brand, length)
        self.test_range = test_range

    def cast_lure(self):
        print(f"Заброс приманки спиннингом {self.brand} тест: {self.test_range}g")

class FeederRod(Rod):
    def __init__(self, brand, length, tip_count):
        super().__init__(brand, length)
        self.tip_count = tip_count

    def feed_fish(self):
        print(f"Закорм рыбы фидерным удилищем {self.brand}, количество вершинок: {self.tip_count}")

my_spinning_rod = SpinningRod("Shimano", 2.7, "5-25")
my_spinning_rod.use()
my_spinning_rod.cast_lure()

my_feeder_rod = FeederRod("Daiwa", 3.6, 3)
my_feeder_rod.use()
my_feeder_rod.feed_fish()
```

### Результат
<img width="789" height="286" alt="image" src="https://github.com/user-attachments/assets/90067cf9-1a2d-4895-babe-8a5a360a8aee" />

### Вывод
Созданы два класса-потомка SpinningRod и FeederRod, наследующие от базового класса FishingRod. Каждый класс-потомок добавляет специфические атрибуты (test_range, tip_count) и методы (cast_lure(), feed_fish()). Использован super() для вызова конструктора родителя.
# Самостоятельная работа 4
## Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Rod:
    def __init__(self, brand, rod_type, length, weight, material, test_range, price):
        self.brand = brand
        self.type = rod_type
        self.length = length
        self.weight = weight
        self.material = material
        self.test_range = test_range
        self.__price = price
        self._warranty_years = 2

    def get_price(self):
        return self.__price

    def get_warranty_info(self):
        return f"Гарантия: {self._warranty_years} года"

    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Тип: {self.type}")
        print(f"Длина: {self.length} м")
        print(f"Вес: {self.weight}")
        print(f"Материал: {self.material}")
        print(f"Тест: {self.test_range}")
        print(f"Цена: {self.get_price()} руб.")
        print(self.get_warranty_info())


rod = Rod("Salmo", "Спиннинг", 2.4, 180, "Карбон", "5-25", 4500)

rod.display_info()
```

### Результат
<img width="764" height="399" alt="image" src="https://github.com/user-attachments/assets/50478009-c408-41f5-84e1-80b0fb6955d3" />

### Вывод
Добавлены приватные (__price) и защищенные (_warranty_years) атрибуты. Реализованы геттеры. 
# Самостоятельная работа 5
## Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Rod:
    def __init__(self, brand, rod_type):
        self.brand = brand
        self.type = rod_type

    def fishing_action(self):
        return f"{self.brand} {self.type}: производит заброс"

    def get_recommendation(self):
        return "Универсальная рекомендация"


class SpinningRod(Rod):
    def __init__(self, brand, length):
        super().__init__(brand, "Спиннинг")
        self.length = length

    def fishing_action(self):
        return f"{self.brand} спиннинг: заброс блесны или воблера"

    def get_recommendation(self):
        return "Идеально для ловли на искусственные приманки"


class FeederRod(Rod):
    def __init__(self, brand, test):
        super().__init__(brand, "Фидер")
        self.test = test

    def fishing_action(self):
        return f"{self.brand} фидер: точный заброс кормушки с прикормкой"

    def get_recommendation(self):
        return "Рекомендуется для донной ловли с кормушкой"


class FlyRod(Rod):
    def __init__(self, brand, line_class):
        super().__init__(brand, "Нахлыст")
        self.line_class = line_class

    def fishing_action(self):
        return f"{self.brand} нахлыст: изящный заброс мушки"

    def get_recommendation(self):
        return "Специализированная снасть для нахлыстовой ловли"


def demonstrate_fishing(rods):
    for rod in rods:
        print(rod.fishing_action())
        print(f"Рекомендация: {rod.get_recommendation()}")
        print("-" * 50)


rods = [
    SpinningRod("Shimano", 2.7),
    FeederRod("Daiwa", "40-80"),
    FlyRod("Hardy", 5),
    Rod("Salmo", "Универсальная")
]

demonstrate_fishing(rods)
```

### Результат
<img width="769" height="501" alt="image" src="https://github.com/user-attachments/assets/64898f6a-63a2-4695-a035-334b392c3136" />

### Вывод
Создана иерархия классов с переопределенными методами fishing_action() и get_recommendation(). Реализована функция demonstrate_fishing(), работающая с объектами разных классов через единый интерфейс.
# Общий вывод
В ходе самостоятельной работы успешно освоены и применены на практике все основные принципы объектно-ориентированного программирования. Создана целостная система классов, демонстрирующая: абстракцию - выделение существенных характеристик удочки, инкапсуляцию - сокрытие внутренней реализации и защита данных, наследование - создание иерархии специализированных классов, плиморфизм - единообразная работа с объектами разных типов.
