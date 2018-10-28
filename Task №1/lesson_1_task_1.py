<<<<<<< HEAD
# Рсчитать площадь треугольника по формуле Герона
line_1 = int(input('Number >>> '))
line_2 = int(input('Number >>> '))
line_3 = int(input('Number >>> '))
p = (line_1 + line_2 + line_3) / 2
s = (p * (p - line_1) * (p - line_2) * (p - line_3)) ** 0.5
print('Ваша площадь сэр >>> %.2f' % s)
=======
# Рсчитать площадь треугольника по формуле Герона
line1 = 14
line2 = 12
line3 = 13
p = (line1 + line2 + line3) / 2
s = (p * (p - line2) * (p - line2) * (p - line3)) ** 0.5
print(s)
>>>>>>> d6dde82cfa360c6ec55e039771f79543f82fa9d0
