import numpy as np

u = np.array([4, 1, 1])
v = np.array([2, 1, 0])

u1, u2, u3 = u
v1, v2, v3 = v

c1 = u2 + v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1)
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print("i 성분:", c1)
print("j 성분:", c2)
print("k 성분:", c3)
print("u x v:", result)

reference = np.cross(u, v)
print("NumPy 결과:", reference)
print("결과 일치:", np.allclose(result, reference))

print("u ' (u x v):", np.dot(u, result))
print("v ' (u x v):", np.dot(v, result))
