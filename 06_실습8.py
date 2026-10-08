import numpy as np

u1 = np.array([1, 1, 0], dtype=float)
u2 = np.array([1, 1, 1], dtype=float)
u3 = np.array([0, 2, 3], dtype=float)

A = np.array([
    u1,
    u2,
    u3
])

print("벡터 행렬 A")
print(A)

det_A = np.linalg.det(A)
det_A = round(det_A, 10)
volume = abs(det_A)

print("\n행렬식 det(A)")
print(det_A)
print("\n평행육면체 S의 체적")
print(volume)