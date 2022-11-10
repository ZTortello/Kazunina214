from random import randint

print("Задание 4")
massiv1 = []
for i in range(10):
    u = randint(-1000, 1000)
    print(u)
    massiv1.append(u)
print("Три меньших значения из списка")
for i in range(3):
    o = min(massiv1)
    print(o)
    massiv1.remove(o)
