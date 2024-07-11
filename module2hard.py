n = int(input())
result = []

for i in range(1, 20):
    if i > n:
        break
    for j in range(i, 20):
        if n % (i + j) == 0:
            if i == j:
                continue
            else:
                result.append(i)
                result.append(j)
print(*result)