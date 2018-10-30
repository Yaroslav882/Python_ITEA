def add(number_1, number_2):
    return number_1 + number_2
def sub(number_1, number_2):
    return number_1 - number_2
def div(number_1 , number_2):
    return number_1 / number_2
def mul(number_1 , number_2):
    return number_1 * number_2

def operation_check(number_1, operation, number_2):
    if operation == '+':
        result = add(number_1, number_2)
    elif operation == '-':
        result = sub(number_1, number_2)
    elif operation == '*':
        result = mul(number_1, number_2)
    elif operation == '/':
            if number_2 == 0:
                result = 'Прости, но правило есть правило, на 0 не делится!'
                print (result)
            else:
                result = div(number_1, number_2)
    else:
        result = 'Ошибочка бро'
        return result
    return result

def again():
    need_again = input('''
    Хочешь еще раз использовать калькулятор?
    Нажми Д если ДА или Н если НЕТ
    ''')
    if need_again == 'Д':
        calculate()
    elif need_again == 'Н':
        print('Спасибо большое, до встречи!')
    else:
        again()

def calculate():
    first_number = float(input('Введите первое число >>> '))
    operation = input('Ваше действие >>> ')
    second_number = float(input('Введите второе число >>> '))
    result = operation_check(first_number, operation, second_number)
    if result != 'Прости, но правило есть правило, на 0 не делится!':
        print('А вот и результат >>> ', result)
    again()

calculate()
