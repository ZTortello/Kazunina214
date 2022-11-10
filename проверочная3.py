from random import randint

print("Задание 3")
massiv = []
for i in range(10):
    y = randint(-1000, 1000)
    print(y)
    massiv.append(y)
print("Три больших значения из списка")
for i in range(3):
    z = max(massiv)
    print(z)
    massiv.remove(z)
