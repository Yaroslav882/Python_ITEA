# Get out of the calculator or not
def again():
    while True:
        cont = input('''
        Do you want to use the calculator again?
        Press Y if YES or N if NO
        ''')
        while cont.lower() in ("yes", "y",):
            return True
        if cont.lower() in ("no", "n"):
            return False
        else:
            print('Please try again')