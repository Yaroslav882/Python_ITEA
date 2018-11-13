# Обычный калькулятор
def add(number_1, number_2):
    return number_1 + number_2
def sub(number_1, number_2):
    return number_1 - number_2
def div(number_1 , number_2):
    return number_1 / number_2
def mul(number_1 , number_2):
    return number_1 * number_2

OPERATION = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul
}

def simple_calculator():
    while True:
        try:
            num_1 = float(input('First number >> '))
            operation = input('Oparation >> ')
            num_2 = float(input('Second number >> '))
            result = None
            result = OPERATION[operation](num_1, num_2)
            print(num_1, operation, num_2, '=', result)
            if not again():
                break
        except (ZeroDivisionError, ValueError, KeyError) as error:
            print('Error >> ', error)
            print('Please try again')

# Найти квадратный корень
def square():
    import math
    while True:
        try:
            answer = float(input("Find the square root of >>> "))
            if answer > 0 or answer < 0:
                print(math.sqrt(answer))
            elif answer == 0:
                print('Captain, the square root of 0 will be 0')
            if not again():
                print('Square exit')
                break
        except (ZeroDivisionError, ValueError) as error:
            print('Error >> ', error)
            print('Please try again')

# Выйти с калькулятора или нет
def again():
    need_again = input('''
    Do you want to use the calculator again?
    Press Y if YES or H if NO
    ''')
    if need_again == 'Y':
        return True
    elif need_again == 'N':
        print('Thank you so much! See you!')
        return False

# Выбор функции
def choice():
    restart = True
    while restart:
        your_choice = input('Your choice >> ')
        if len(your_choice) == 0:
            print('Something went wrong, check your choice!')
            continue
        if your_choice == 'Calculator':
            simple_calculator()
        elif your_choice == 'Square':
            square()
        elif your_choice == 'Exit':
            return
        else:
            print('Something went wrong, check your choice!')
            restart = True

print('Welcome to the mini calculator. There are two functions')
print('''
"Calculator" - select it to enable the simple calculator
"Square" - choose it to find the square root of a number
"Exit" - if you want to exit the program
''')

choice()