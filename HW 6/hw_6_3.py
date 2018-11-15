""" Задание №3.
Создать функцию, которая анализирует параметры и если хотя-бы один из них
другого типа, то вызывает исключение (на выбор - одно из стандартных или своё
собственное по примеру Задания №2).
В комментарии обосновать свой выбор.

В функции main() независиимо от того было исключение или не было,
всё-равно надо сообщить с какими аргументами вы вызывали свою функцию и
какого типа был каждый аргумент.
"""

def check_params_type(*args):
    type_set = set()
    for gum in args:
        type_set.add(type(gum))
    if len(type_set) > 1:
        raise TooManyTypes(type_set)
    return type_set

class TooManyTypes(Exception):
    def __init__(self, type_set):
        self.type_set = type_set

def main(*args):
    try:
        check_params_type(*args)
    except TooManyTypes as error:
        print(format(error.type_set))
    finally:
        for gum in args:
            print("Element '{}' refers to type {}.".format(gum,type(gum)))


if __name__ == "__main__":
    main(1, '1', 114.3, True)
