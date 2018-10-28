# 3. Решение уровнения ax^2 + bx + c = 0
a = float(input("Введите значение a = "))
b = float(input("Введите значение b = "))
c = float(input("Введите значение c = "))
discrim = b**2 - 4 * a * c
print("Дискриминант D = %.2f" % discrim)
if discrim > 0:
	import math
	x1 = (-b + math.sqrt(discrim)) / (2 * a)
	x2 = (-b - math.sqrt(discrim)) / (2 * a)
	print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discrim == 0:
	x = -b / (2 * a)
	print("x = %.2f" % x)
else:
    print("Сорри, корней тут нет")
