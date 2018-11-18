# Runs a regular calculator
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
            operation = operation.replace(' ', '')
            num_2 = float(input('Second number >> '))
            result = None
            result = OPERATION[operation](num_1, num_2)
            print(num_1, operation, num_2, '=', result)
            if not again():
                break
        except (ZeroDivisionError, ValueError, KeyError) as error:
            print('Error >> ', error)
            print('Please try again')

# Get out of the calculator or not
def again():
    need_again = input('''
    Do you want to use the calculator again?
    Press Y if YES or N if NO
    ''').lower()
    if need_again == 'Y':
        return True
    elif need_again == 'N':
        print('Thank you so much! See you!')
        return False