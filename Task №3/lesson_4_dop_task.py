star_1 = int(input('Введите первое число >>> '))
star_2 = int(input('Введите второе число >>> '))

print('И вот что вышло!')
for i in range(star_1):
    for j in range(star_2):
        print('*', end=' ')
    print()