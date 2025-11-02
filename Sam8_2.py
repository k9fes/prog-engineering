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