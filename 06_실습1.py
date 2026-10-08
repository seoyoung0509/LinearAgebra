import numpy as np

np.set_printoptions(suppress=True, precision=2)
A = np.array([
    [1, 2, 3],
    [2, 5, 3],
    [1, 0, 8]
], dtype=float)

I = np.eye(3)

AI = np.hstack((A, I))

def show_matrix(operation):
    """행 연산 과정 출력"""
    print(f"\n{operation}")
    print(AI)

print("초기 첨가행렬 [A | I]")
print(AI)

AI[1] = (-2) * AI[0] + AI[1]
show_matrix("R2 ← (-2)R1 + R2")

AI[2] = (-1) * AI[0] + AI[2]
show_matrix("R3 ← (-1)R1 + R3")

AI[2] = 2 * AI[1] + AI[2]
show_matrix("R3 ← 2R2 + R3")

AI[2] = (-1) * AI[2]
show_matrix("R3 ← (-1)R3")
show_matrix("R2 ← R2 + 3R3")

AI[0] = AI[0] - 3 * AI[2]
show_matrix("R1 ← R1 - 3R3")

AI[0] = AI[0] - 2 * AI[1]
show_matrix("R1 ← R1 - 2R2")

A_inverse = AI[:, 3:]

print("\n최종 첨가행렬 [I | A^(-1)]")
print(AI)

print("\nA의 역행렬")
print(A_inverse)

print("\n검산: A × A^(-1)")
print(A @ A_inverse)