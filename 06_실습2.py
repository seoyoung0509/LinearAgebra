import numpy as np

np.set_printoptions(suppress=True, precision=2)

A = np.array([
    [1, -3, 4],
    [2, -5, 7],
    [0, -1, 1]
], dtype=float)

I = np.eye(3)

AI = np.hstack((A, I))

def show_matrix(title):
    """첨가행렬을 [A | I] 형태로 출력"""
    print(f"\n{title}")
    
    for row in AI:
        left = " ".join(f"{value:6.1f}" for value in row[:3])
        right = " ".join(f"{value:6.1f}" for value in row[3:])
        print(f"[{left} | {right}]")

show_matrix("초기 첨가행렬 [A | I]")

AI[1] = (-2) * AI[0] + AI[1]
show_matrix("1단계: R2 ← (-2)R1 + R2")

AI[2] = AI[1] + AI[2]
show_matrix("2단계: R3 ← R2 + R3")

AI[0] = 3 * AI[1] + AI[0]
show_matrix("3단계: R1 ← 3R2 + R1")

left_matrix = AI[:, :3]
right_matrix = AI[:, 3:]

print("\n행 연산 후 왼쪽 행렬")
print(left_matrix)
print("\n행 연산 후 오른쪽 행렬")
print(right_matrix)

if np.linalg.matrix_rank(A) < A.shape[0]:
    print("\n판정 결과")
    print("A의 행들이 선형종속입니다.")
    print("왼쪽 행렬에 모든 원소가 0인 행이 발생했습니다.")
    print("따라서 A를 단위행렬로 만들 수 없습니다.")
    print("행렬 A의 역행렬은 존재하지 않습니다.")
else:
    A_inverse = right_matrix
    print("\nA의 역행렬")
    print(A_inverse)

det_A = np.linalg.det(A)
print("det(A) =", round(det_A))