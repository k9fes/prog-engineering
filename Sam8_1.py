class  Rod:

    def __init__(self, manufacturers, type):
        self.manufacturers = manufacturers
        self.type = type

my_rod = Rod("Shimano", "Feeder")

print(f"Производитель: {my_rod.manufacturers}")
print(f"Тип: {my_rod.type}")
