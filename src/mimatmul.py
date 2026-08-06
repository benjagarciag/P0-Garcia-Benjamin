def mimatmul(A, B):
    if not A or not B:
        return []
    filas_a = len(A)
    cols_a = len(A[0])
    filas_b = len(B)
    cols_b = len(B[0])

    if cols_a != filas_b:
        raise ValueError("Las columnas de A deben coincidir con las filas de B")

    C = [[0 for _ in range(cols_b)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += A[i][k] * B[k][j]
    return C
