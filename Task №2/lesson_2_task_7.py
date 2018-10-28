# 7. Высокосный год или нет
year = int(input('Введите год - '))
if year % 4 != 0:
    print("Обычный год")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Высокосный год")
    else:
        print("обычный год")
else:
    print("Высокосный год")