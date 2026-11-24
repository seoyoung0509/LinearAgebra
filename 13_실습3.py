import numpy as np

u = np.array([3, 1, 0])
v = np.array([1, 3, 2])

cross_product = np.cross(u, v)

squared_length = np.dot(cross_product, cross_product)
area = np.linalg.norm(cross_product)

print("u x v =", cross_product)
print(f"넓이의 제곱 = {squared_length}")
print(f"평행사변형의 넓이 = {area:.6f}")