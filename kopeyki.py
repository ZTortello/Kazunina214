task = int(input("Введите задание: "))
match (task):
    case 1:
        god = int(input("Введите год от -2000 до 2000: "))
        if -2000 <= god <= 2000:
            if god % 4 == 0:
                print("Год високосный")
            else:
                print("Нет")
        else:
            print('Написано же от -2000 до 2000')
    case 2:
        kop = int(input("Введте сколько у вас копеек"))
        ostatok = kop % 10
        if 11 <= kop <= 19:
            print(f"{kop} копеек")
        elif ostatok == 1:
            print(f"{kop} копейка")
        elif 2 <= ostatok <= 4:
            print(f"{kop} копейки")
        elif 5 <= ostatok <= 9 or ostatok == 0:
            print(f"{kop} копеек")
        elif kop >= 100:
            print("Вы богатый")
        elif kop <= 0:
            print("вы нищий")
    case 3:
        day = int(input("Введите день года: "))
        if day < 0 or day > 365:
            print("НЕТ")
        else:
            while day>=7:
                day = day -7
            if day == 0:
                print("Воскресенье")
            if day == 1:
                print("Понедельник")
            if day == 2:
                print("Вторник")
            if day == 3:
                print("Отсылка на wednesday?")
            if day == 4:
                print("Сосдай")
            if day == 5:
                print("Фридай")
            if day == 6:
                print("Сатурдай")
    case 4:
        for i in range(1, 1001):
            for k in range(i, 1001):
                z = i ** 2 + k ** 2
                c = int(z ** 0.5)
                if c <= 1000 and c * c == z:
                    a = i
                    b = k
                    while a != 0 and b != 0:
                        if a > b:
                            a = a % b
                        else:
                            b = b % a
                    a += b
                    if a == 1:
                        print(i, k, c)
    case 5:
        import math
        e = math.e
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        F = (((2 + y)**2 + math.sin(y+5)**(1/7))**0.5)/(math.log(x + 1,e) - y**3)
        print(F)
    case 6:
        a = int(input("Введите а: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        d = b**2 - 4 * a * c
        if d == 0:
            print(-b / 2*a)
        elif d < 0:
            print("корней нет")
        elif d > 0:
            x1 = (-b + (d)**0.5)/(2*a)
            x2 = (-b - (d) ** 0.5) / (2 * a)
        print(f"x1 = {x1} \n x2 = {x2}")
    case 7:
        import random
        list = []
        k = 0
        for i in range(5000):
            p = random.randint(1, 259)
            list.append(p)
        print(list)
        while k != 4999:
            for i in range(4999):
                n1 = list[i]
                n2 = list[i + 1]
                if n1 > n2:
                    del list[i]
                    list.insert(i + 1, n1)
            for j in range(1, 4999):
                h = len(list)
                n1 = list[h - j]
                n2 = list[h - j - 1]
                if n1 < n2:
                    del list[h - j]
                    list.insert(h - j - 1, n1)
            k = k + 1
        print(list)