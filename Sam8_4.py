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

