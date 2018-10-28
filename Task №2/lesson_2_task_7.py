<<<<<<< HEAD
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
=======
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
>>>>>>> d6dde82cfa360c6ec55e039771f79543f82fa9d0
    print("Высокосный год")