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
    bush = TomatoBush(4)  # Куст с 4 томатами
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

