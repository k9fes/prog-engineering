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