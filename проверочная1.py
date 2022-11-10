import math

print("Задание один")
a = (101 + 0) / 3
print(a)
b = 3.0 * math.e - 6 * 10000000000.1
print(b)
c1 = True
c2 = True
c3 = c1 and c2
print(c3)
d1 = False
d2 = c1 and d1
print(d2)
e = (d1 and d1) or (c1 and c1)
print(e)
f = (d1 or d1) and (c1 or c1)
print(f)
