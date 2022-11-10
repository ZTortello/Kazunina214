from random import randint

print("Задание 7")
massiv = []
for i in range(10):
    y = randint(-1000, 1000)
    print(y)
    massiv.append(y)
for i in range(10):
    if (massiv[i] % 2) == 0:
        print("Число", massiv[i], "четное")
    else:
        print("Число", massiv[i], "нечетное")
