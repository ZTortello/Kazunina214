import math

print("Введите вес (кг) и рост (см) тела")
a = float(input())
b = float(input())
m = b / 100
c = a / math.sqrt(m)
print("Индекс массы тела", c)
