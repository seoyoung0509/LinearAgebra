import numpy as np

np.set_printoptions(suppress=True, precision=2)

A = np.array([
    [1, -1, 1],
    [1, 1, -2],
    [1, 2, 1]
], dtype=float)

b = np.array([0, 1, 6], dtype=float)
D = round(np.linalg.det(A))

print("계수행렬 A")
print(A)
print("\n상수벡터 b")
print(b)
print(f"\nD = det(A) = {D}")

if D == 0:
    print("det(A)가 0이므로 크래머의 규칙을 적용할 수 없습니다.")
else:
    determinants = []
    solution = []
    for i in range(A.shape[1]):
        Ai = A.copy()
        Ai[:, i] = b

        Di = round(np.linalg.det(Ai))
        xi = Di / D
        determinants.append(Di)
        solution.append(xi)

        print(f"\n{i + 1}번째 열을 b로 교체")
        print(Ai)
        print(f"D{i + 1} = det(A{i + 1}) = {Di}")
        print(
            f"x{i + 1} = D{i + 1}/D "
            f"= {Di}/{D} = {xi}"
        )
    
    solution = np.array(solution)

    print("\n최종 해")
    for i, value in enumerate(solution, start=1):
        print(f"x{i} = {value}")

    print("\n검산 결과 A @ x")
    print(A @ solution)
    print("\n원래 상수벡터 b")
    print(b)