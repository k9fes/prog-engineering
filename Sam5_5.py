def set(numbers):
    result = set()
    for num in set(numbers):
        count = numbers.count(num)
        for i in range(1, count + 1):
            if i == 1:
                result.add(num)
            else:
                result.add(str(num) * i)
    return result
melon = [
    [1, 1, 3, 3, 1],
    [5, 5, 5, 5, 5, 5, 5],
    [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
]

for i, lst in enumerate(melon, 1):
    print(f"Список {i}: {set(lst)}")