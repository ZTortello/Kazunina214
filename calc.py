import math

print("Какую команду вы хотите исполнить? "
      "Введите 1: Сумма двух чисел. "
      "Введите 2: Вычитание одного числа из другого. "
      "Введите 3: Умножение двух чисел. Введите 4: "
      "Деление одного числа на другое. Введите 5: "
      "Решение квадратного уравнения")
number = int(input())
if number == 1:
    print("Введите первое слагаемое")
    term1 = float(input())
    print("Введите второе слагаемое")
    term2 = float(input())
    summ = term1 + term2
    print(summ)
elif number == 2:
    print("Введите уменьшаемое")
    min1 = float(input())
    print("Введите вычитаемое")
    min2 = float(input())
    resid = min1 - min2
    print(resid)
elif number == 3:
    print("Введите первый множитель")
    fac1 = float(input())
    print("Введите второй множитель")
    fac2 = float(input())
    multi = fac1 * fac2
    print(multi)
elif number == 4:
    print("Введите делимое")
    div1 = float(input())
    print("Введите делитель")
    div2 = float(input())
    divide = div1 / div2
    print(divide)
elif number == 5:
    print("Введите значение a")
    a = float(input())
    print("Введите значение b")
    b = float(input())
    print("Введите значение c")
    c = float(input())
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("Корней нет")
else:
    print("Такой функции нет!")
