# Тема 9. ООП на Python: концепции, принципы и примеры реализации
Отчёт по Теме 8 выполнил:
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
## Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию  init (), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python
class Kostya:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Kostya':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Kostya"

person1 = Kostya('Alex')
person2 = Kostya('Kostya')
print(person1.name)
print(person2.name)

person2.supername = 'Zaspanov'
```
### Результат
<img width="520" height="371" alt="image" src="https://github.com/user-attachments/assets/6ca0c631-c619-4dc3-a155-f233768b926b" />

# Лабораторные работа 2
##   Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе  реализуйте  метод,  выводящий  на  печать  «Мороженое  с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient=None, price=100):
        self.price = price
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}, цена: {self.price + 30}")
        else:
            print(f"Обычное мороженое, цена: {self.price}")

icecream1 = Icecream()
icecream1.composition()
icecream2 = Icecream('фисташкой')
icecream2.composition()
icecream3 = Icecream(5)
icecream3.composition()
```
### Результат
<img width="707" height="255" alt="image" src="https://github.com/user-attachments/assets/8f6437cb-da67-41eb-b338-f4996a136388" />

# Лабораторные работа 3
## Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка. 

```python
class Myclass():
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = Myclass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value() #этот метод удаляет атрибут _value из объекта obj
print(obj.get_value()) #метод пытается вернуть значение self._value, но этот атрибут уже был удален на предыдущем шаге
#Результат: возникает ошибка потому что Python не может найти атрибут _value в объекте, так как он был явно удален
```
### Результат
<img width="706" height="476" alt="image" src="https://github.com/user-attachments/assets/9a10a3bf-e16b-481c-b948-f7d4acb4ffeb" />

# Лабораторные работа 4
## Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    def __init__(self, species):
        self.species = species

    def info(self):
        return f"Это млекопитающее: {self.species}"


class Cat(Mammal):
    def __init__(self, name, breed, jump):
        super().__init__("Кошка")
        self.name = name
        self.breed = breed
        self.jump = jump

    def info(self):
        return f"{super().info()}, имя: {self.name}, порода: {self.breed}, прыжок: {self.jump}м"


class Dog(Mammal):
    def __init__(self, name, weight, bark_loudness="громко"):
        super().__init__("Собака")
        self.name = name
        self.weight = weight
        self.bark_loudness = bark_loudness

    def info(self):
        return f"{super().info()}, имя: {self.name}, вес: {self.weight}кг, лает: {self.bark_loudness}"

cat = Cat("Барсик", "Персидская", 1.5)
dog = Dog("Рекс", 25, "очень громко")

print(cat.info())
print(dog.info())
```
### Результат
<img width="796" height="224" alt="image" src="https://github.com/user-attachments/assets/43405147-bd27-4a5c-b404-6edd769f6e8d" />

# Лабораторные работа 5
## На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

Ivan = Russian()
greet(Ivan)
John = English()
greet(John)
```
### Результат
<img width="553" height="225" alt="image" src="https://github.com/user-attachments/assets/a136de1b-fd74-46e6-9ec7-a467b83a4f2f" />


# Самостоятельная работа 1
## Садовник и помидоры

```python
class Tomato:
    # Статическое свойство со стадиями созревания
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зелёный',
        3: 'красный'
    }

    def __init__(self, index):
        # _index - защищенное свойство (передается параметром)
        # _state - защищенное свойство (начальное значение из states)
        self._index = index+1
        self._state = 0  # Начинаем со стадии "отсутствует"

    def grow(self):
         #Переводит томат на следующую стадию созревания
        if self._state < 3:  # Если не достигли конечной стадии
            self._state += 1
        print(f'Томат {self._index} теперь на стадии: {Tomato.states[self._state]}')

    def is_ripe(self):
        #Проверяет, созрел ли томат
        return self._state == 3  # 3 = Красный - значит созрел


class TomatoBush:
    def __init__(self, num_tomatoes):
        # tomatoes - динамическое свойство (список объектов Tomato)
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        #Переводит все томаты на следующую стадию
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        #Проверяет, все ли томаты созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        #Очищает список томатов после сбора урожая
        self.tomatoes = []


class Gardener:
    @staticmethod
    def knowledge_base():
        #справка по садоводству
        print("Справка по садоводству:")
        print("- Поливайте растения регулярно")
        print("- Убедитесь, что достаточно солнечного света")
        print("- Собирайте урожай, когда все томаты красные")
        print("- Не забывайте ухаживать за растениями ежедневно\n")

    def __init__(self, name, plant):
        # name - публичное свойство
        # _plant - защищенное свойство (объект TomatoBush)
        self.name = name
        self._plant = plant

    def work(self):
        #Садовник работает, растение растет
        print(f"{self.name} работает...")
        self._plant.grow_all()

    def harvest(self):
        #Сбор урожая
        if self._plant.all_are_ripe():
            print("Все томаты созрели. Урожай собран!")
            self._plant.give_away_all()
        else:
            print("Еще не все томаты созрели! Продолжайте ухаживать.")



if __name__ == "__main__":
    # 1) Вызываем справку по садоводству
    Gardener.knowledge_base()

    # 2) Создаем объекты классов
    bush = TomatoBush(5)  # Куст с 4 томатами
    gardener = Gardener("Miyabi", bush)

    print(f"Садовник {gardener.name} начинает работу с {len(bush.tomatoes)} томатами\n")

    # 3) Ухаживаем за кустом
    print("--- Первый день ухода ---")
    gardener.work()

    # 4) Пробуем собрать урожай
    print("\n--- Попытка сбора урожая ---")
    gardener.harvest()

    # Продолжаем ухаживать
    print("\n--- Второй день ухода ---")
    gardener.work()

    print("\n--- Третий день ухода ---")
    gardener.work()

    # 5) Собираем урожай
    print("\n--- Попытка сбора урожая ---")
    gardener.harvest()
```

### Результат

### Вывод

# Общий вывод
