from random import randint

massiv2 = []
for i in range(10):
    p = randint(-1000, 1000)
    print(p)
    massiv2.append(p)
print("Среднее значение элементов списка")
g = sum(massiv2)/10
print(g)
print("Значения, превышающие среденее значение списка")
for i in range(10):
    if massiv2[i] > g:
        print(massiv2[i])
        massiv2.remove(massiv2[i])
    else:
        massiv2.remove(massiv2[i])
