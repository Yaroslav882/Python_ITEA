def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3
    print(x)

def main():
    for i in range(-10, 11):
        i /= 2
        y = function(i)
        print('function(', i, ') = ', y, sep='')
main()