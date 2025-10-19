def melon(tpl):
    avg = sum(tpl) / len(tpl)
    return tuple(x for x in tpl if x > avg)

print(melon((131, 4141, 16611, 1441, 242)))
print(melon((10, 10, 10, 10)))
print(melon((1, 2, 3, 4, 5)))