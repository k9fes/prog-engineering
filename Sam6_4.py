def melon(tpl, element):
    if element not in tpl:
        return ()
    index = tpl.index(element)
    try:
        index2 = tpl.index(element, index + 1) + 1
    except ValueError:
        return tpl[index:]
    return tpl[index:index2]

print(melon((1, 2, 3), 8))
print(melon((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(melon((1, 2, 8, 5, 1, 2, 9), 8))
