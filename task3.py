
def cal_det2to2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    print(f"\nTask 3 : Determinant of X^T * X = {det}")
    return det