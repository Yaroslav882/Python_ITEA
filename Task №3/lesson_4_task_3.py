print("Квадрат")
for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print("\n", end="")
print("\n")

print("Прямогульный треугольник")
for i in range(1, 10):
    for j in range(1, 1 + i):
        print('#', end=" ")

    print("\n", end="")
print("\n")

print("Равнобедренный треугольник")
for i in  range(1, 11):
    for j in range(11 - i):
        print(" ", end= " ")
    for j in range(1, i):
        print("@", end= " ")
    for i in range(i, 0, -1):
        print("@", end= " ")

    print("\n", end="")