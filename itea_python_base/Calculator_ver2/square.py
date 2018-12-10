from again import again

# Find the square root of a number
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
