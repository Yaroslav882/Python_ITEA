# Рсчитать площадь треугольника по формуле Герона
line_1 = int(input('Number >>> '))
line_2 = int(input('Number >>> '))
line_3 = int(input('Number >>> '))
p = (line_1 + line_2 + line_3) / 2
s = (p * (p - line_1) * (p - line_2) * (p - line_3)) ** 0.5
print('Ваша площадь сэр >>> %.2f' % s)