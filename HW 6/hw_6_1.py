""" Задание №1.
функция что-то делает со строкой и для непечатных символов (string.whitespace)
вызывает исключение ValueError
"""
from string import whitespace

def string_processing(text, *args, **kwargs):
    result = text.upper() + " - Cool bro!"
    if list(set(whitespace) & set(text)):
        raise ValueError("- Warming! Spescial symbol!")
    return result

text = 'assdf aw'

if __name__ == "__main__":
    try:
        print(string_processing(text))
    except ValueError as error:
        print(text, error)