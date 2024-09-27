def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        matrix.append(row)

        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
matrix = get_matrix(2, 2, 10)
print(matrix)
