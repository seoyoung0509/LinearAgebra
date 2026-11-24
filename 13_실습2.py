import numpy as np

u = np.array([3, -1, 2])
v = np.array([1, -2, 4])

u1, u2, u3 = u
v1, v2, v3 = v

c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print("i 성분:", c1)
print("j 성분:", c2)
print("k 성분:", c3)
print("u x v:", result)

print("NumPy 결과:", np.cross(u, v))

print("u ' (u x v):", np.dot(u, result))
print("v ' (u x v):", np.dot(v, result))