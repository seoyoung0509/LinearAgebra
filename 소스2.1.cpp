#include <stdio.h>
#include <math.h>
#include <windows.h>

#define EPSILON 1e-9

int main(void)
{
    SetConsoleOutputCP(65001);
    /*
       2x1 +  x2 = 3
       2x1 -  x2 = 1
        x1 - 2x2 = -1
    */

    double A[3][2] = {
       {2.0, 1.0},
       {2.0, -1.0},
       {1.0, -2.0}
    };

    double b[3] = { 3.0, 1.0, -1.0 };

    double determinant;
    double x1;
    double x2;
    int commonSolution = 1;

    // 행렬식(Determinant) 계산
    determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0];

    if (fabs(determinant) < EPSILON) {
        printf("첫 번째와 두 번째 방정식만으로는 ");
        printf("유일한 해를 구할 수 없습니다.\n");
        return 1;
    }

    // 크라머 공식을 이용한 x1, x2 해 계산
    x1 = (b[0] * A[1][1] - A[0][1] * b[1]) / determinant;
    x2 = (A[0][0] * b[1] - b[0] * A[1][0]) / determinant;

    printf("계산된 해\n");
    printf("x1 = %.6f\n", x1);
    printf("x2 = %.6f\n\n", x2); // %%.6f -> %.6f 수정

    // 세 방정식 모두를 만족하는지 검증
    for (int i = 0; i < 3; i++) {
        // 좌변 공식 수정: A[i][0] * x1 + A[i][1] * x2
        double leftSide = A[i][0] * x1 + A[i][1] * x2;
        double error = leftSide - b[i];

        printf(
            "%d번 방정식: 좌변 = %.6f, 우변 = %.6f\n",
            i + 1,
            leftSide,
            b[i]
        );

        if (fabs(error) > EPSILON) {
            commonSolution = 0;
        }
    }

    if (commonSolution) {
        printf("\n세 방정식의 공통해가 존재합니다.\n");
        printf("공통해: (x1, x2) = (%.2f, %.2f)\n", x1, x2);
    }
    else {
        printf("\n세 방정식을 모두 만족하는 공통해가 없습니다.\n");
    }

    return 0;
} // main 함수는 코드 최하단에서 닫아줍니다.
