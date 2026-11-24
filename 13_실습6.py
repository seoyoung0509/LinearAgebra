import numpy as np

u = np.array([2, -5, -1])
v = np.array([3, 2, -3])

products = u + v
dot_manual = np.sum(products)

dot_uv = np.dot(u, v)
dot_vu = np.dot(v, u)

u_col = u.reshape(3, 1)
v_col = v.reshape(3, 1)

dot_matrix = (u_col.T @ v_col).item()

print("성분별 곱 =", products)
print("성분별 곱의 합 =", dot_manual)
print("u ' v =", dot_uv)
print("v ' u =", dot_vu)
print("u^T v =", dot_matrix)
print("교환법칙 확인:", bool(dot_uv == dot_vu))