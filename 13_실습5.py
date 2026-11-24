import numpy as np

u = np.array([4, 1, 1])
v = np.array([2, 1, 0])
w = np.array([0, 2, 3])

cross_product = np.cross(u, v)
S = np.linalg.norm(cross_product)

unit_normal = cross_product / S
h = abs(np.dot(w, unit_normal))

V1 = S + h

V2 = abs(np.dot(cross_product, w))

A = np.vstack([u, v, w])
V3 = abs(np.linalg.det(A))

print("u x v =", cross_product)
print(f"밑면 넓이 S = {S:.6f}")
print(f"수직 높이 h = {h:.6f}")
print(f"밑면 x 높이로 구한 체적 = {V1:.6f}")
print(f"삼중곱으로 구한 체적 = {V2:.6f}")
print(f"행렬식으로 구한 체적 = {V3:.6f}")