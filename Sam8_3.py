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