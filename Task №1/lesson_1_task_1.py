# Рсчитать площадь треугольника по формуле Герона
line1 = 14
line2 = 12
line3 = 13
p = (line1 + line2 + line3) / 2
s = (p * (p - line2) * (p - line2) * (p - line3)) ** 0.5
print(s)