import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

def get_minor(matrix, row, col):
    return np.delete(
        np.delete(matrix, row, axis=0),
        col,
        axis=1
    )

def cofactor_matrix(matrix):
    n = matrix.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            C[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    return C

det_A = round(np.linalg.det(A))

if det_A == 0:
    print("행렬식이 0이므로 역행렬이 존재하지 않습니다.")
else:
    C = cofactor_matrix(A)
    adj_A = C.T
    inverse_A = (1 / det_A) * adj_A
    C = np.round(C, 10)
    adj_A = np.round(adj_A, 10)
    inverse_A = np.round(inverse_A, 10)

    print("행렬 A")
    print(A)
    print("\n행렬식 det(A)")
    print(det_A)
    print("\n여인수행렬 C")
    print(C)
    print("\n수반행렬 adj(A)")
    print(adj_A)
    print("\n역행렬 A^(-1)")
    print(inverse_A)
    print("\n검산 A × A^(-1)")
    print(np.round(A @ inverse_A, 10))