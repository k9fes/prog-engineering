def melon(*melon):
    if not melon:
        return 0
    return sum(melon) / len(melon)

if __name__ == '__main__':
    print(melon(165, 15151, -141, 21424,21))