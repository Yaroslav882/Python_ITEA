# 4. Запросить у пользователя два числа
numb_1 = int(input('Введите первое число - '))
numb_2 =int(input('Введите второе число - '))
if numb_1 > numb_2:
    numb_3 = numb_1 - numb_2
    print('Ваше число -', numb_3)
elif numb_1 < numb_2:
    numb_3 = numb_1 + numb_2
    print('Ваше число -', numb_3)
elif numb_1 == numb_2:
    print('Дружие твои числа равны')