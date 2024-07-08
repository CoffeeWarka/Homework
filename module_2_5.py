def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2,3,7)
result2 = get_matrix(5,4,8)
result3 = get_matrix(1,2,4)
print(result1)
print(result2)
print(result3)