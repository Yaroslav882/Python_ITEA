from square import square
from simple_calculator import simple_calculator

# What to do a calculator? Your choice
def choice():
    restart = True
    while restart:
        your_choice = input('Your choice >> ')
        if len(your_choice) == 0:
            print('Something went wrong, check your choice!')
            continue
        if your_choice.lower() == 'Calculator':
            simple_calculator()
        elif your_choice.lower() == 'Square':
            square()
        elif your_choice.lower() == 'Exit':
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