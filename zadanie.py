from random import randint

a = []
sum1 = 0
sum2 = 0
del1 = 0
del2 = 0
for i in range(10):
    b = randint(-1000, 1000)
    a.append(b)
for i in range(10):
    if a[i] == 0:
        while a[i] == 0:
            b = randint(-1000, 1000)
a.append(-1000)
print(a)
for i in range(11):
    if a[i] > 0:
        sum1 = sum1 + a[i]
        del1 = del1 + 1
    elif a[i] < 0:
        sum2 = sum2 + a[i]
        del2 = del2 + 1
c = sum1 / del1
v = sum2 / del2
print(c)
print(v)
