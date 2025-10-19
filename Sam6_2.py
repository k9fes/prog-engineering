def melon(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

print(melon((1, 2, 3), 1))
print(melon((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(melon((2, 4, 6, 6, 4, 2), 9))