def fix_melon(grades):
    return [4 if g == 3 else g for g in grades if g != 2]

melon =[[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
        [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
        [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]]


for i, lst in enumerate(melon, 1):
    print(f"Список {i}: {fix_melon(lst)}")