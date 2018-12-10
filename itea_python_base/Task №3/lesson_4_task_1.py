# Большой код
numbers_a = int(input('Number A >>> '))
numbers_b = int(input('Number B >>> '))
sum_numbs = 0
while numbers_a <= numbers_b:
    if numbers_a == numbers_b:
        print(numbers_b, end='\n')
    else:
        print(numbers_a, end='+')
    sum_numbs += numbers_a
    numbers_a = numbers_a + 1
print('Your sum >>> ', sum_numbs)
print()

# Приятный глазу код
first = int(input("Number A >>> "))
second = int(input("Number B >>>  "))
print(sum(range(first, second + 1)))
