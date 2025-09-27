mellow = int(input())
if not 0 <= mellow <= 10:
    print("Число не в диапазоне")
    exit()
if mellow <= 3:
    print("от 0 до 3")
elif mellow < 6:
    print("от 3 до 6")
else:
    print("от 6 до 10")