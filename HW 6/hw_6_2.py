""" Задание №2.
Переделать Задание №1 с созданием и использованием собственное исключение
WhitespaceError с атрибутами:
    position - позиция в строке
    symbol - какой именно непечатный символ
Функция main() демонстрирует работу вашей функции, должна красиво показывать
что именно вызвало исключение.
"""

from string import whitespace

text = """Hello Nice_to_see_you!"""

class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


def string_processing(text, *args, **kwargs):
    result = "** " + text.upper() * 3 + " **"
    for sym in text:
            if sym in whitespace:
                raise WhitespaceError(text.find(sym) + 1, repr(sym))
    return result


def main():
    try:
        result = string_processing(text, whitespace)
        print("\nYour text", result)
    except WhitespaceError as e:
        print("\nWarming! Spescial symbol! his number {}, his representation - {}".format(e.position, e.symbol))

if __name__ == "__main__":
    main()

