p = [1, -34, 8, 14, -5]
count = 0
for i in range(len(p) -1):
    if (p[i] > 0 and p[i + 1] < 0) or (p[i] < 0 and p[i + 1] > 0) :
        count += 1
print(count)
