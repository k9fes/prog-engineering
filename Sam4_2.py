import random

def melon():
    value = random.randint(1, 6)
    print(f"Выпало: {value}")
    if value in [5, 6]:
        print("Вы победили")
    elif value in [3, 4]:
       melon()
    else:  # 1 или 2
        print("Вы проиграли")

if __name__ == '__main__':
    melon()