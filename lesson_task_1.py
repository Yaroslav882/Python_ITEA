# Рсчитать площадь треугольника по формуле Герона
line1 = 14
line2 = 12
line3 = 13
p = (line1 + line2 + line3) / 2
s = (p * (p - line2) * (p - line2) * (p - line3)) ** 0.5
print(s)

# # Поменять местами значения двух переменных
a = 8
b = 12
b = a + b
a = b - a
b = b - a
print('a' " -", a)
print('b' " -", b)

# Поменять местами значения двух числовых переменных без использования третьей
a = 22
b = 15
a , b = b , a
print('a' , a)
print('b' , b)

# Если число четное, вывести его квадрат, а если нечетное - его удвоенное значение (*)
# Вариант Первый
numbers1 = int(input("Press button - 8 "))
sum1 = numbers1 ** 2
print("Your number -", sum1)
numbers2 = int(input("Press button - 7 "))
sum2 = numbers1 * 2
print("Your number -", sum2)

# Вариант Второй
numbers1 = int(input("Enter number " ))
if (numbers1 % 2) == 0:
    print(numbers1 ** 2)
else:
    print(numbers1 * 2)