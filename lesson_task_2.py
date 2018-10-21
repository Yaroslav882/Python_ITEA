# 1. Совпадение имен
your_name = input('Введите свое имя - ')
my_name = 'Ярослав'
if your_name == my_name:
    print('Юху бро, мы с тобой тески!')
else:
    print('Сорри дружище, другие именя не признаю')

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

# 5. Напишите программу для запроса данных у пользователя с последующим выводом их на печать
name = input('Укажите свое имя сэр - ')
age = int(input('Сколько лет тебе дитя? - '))
city = input('В каком городе ты сейчас живешь? - ')
print()
print('Все корректно?')
print('Ваше имя - {}'.format(name))
print('Ваш возраст -  {}'.format(age))
print('Вы проживаете в - {}'.format(city))

# 6. Присвоить переменной number любое число от 0 до 5.
number = [0, 1, 2, 3, 4, 5]
number_2 = int(input('Введите ваше число - '))
if number_2 == 0:
    print('Ваша цифар {} = {}'.format(number_2, 0))
elif number_2 == 1:
    print('Ваша цифар {} = {}'.format(number_2, 1))
elif number_2 == 2:
    print('Ваша цифар {} = {}'.format(number_2, 2))
elif number_2 == 3:
    print('Ваша цифар {} = {}'.format(number_2, 3))
elif number_2 == 4:
    print('Ваша цифар {} = {}'.format(number_2, 4))
elif number_2 == 5:
    print('Ваша цифар {} = {}'.format(number_2, 5))
else:
    print('Что то пошло не так')

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