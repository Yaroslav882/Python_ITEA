def you_name():
    while True:
        name = input("Введи свое имя >>> ")
        if not name:
            print('Меня звать Ярослав. А тебя как?')
        else:
            print('Приятно познакомиться', name)
            break
you_name()