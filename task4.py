import numpy as np
def cal_inverse(x , det):
    if det == 0:
        print("Task 4 : Inverse does not exist (determinant is zero)\n")
        return None
    
    inv_det = 1 / det
    inv = np.array([[x[1][1] * inv_det, -x[0][1] * inv_det] , [-x[1][0] * inv_det, x[0][0] * inv_det]])

    print(f"Task 4 : Inverse of X^T * X = \n{inv}\n")
    return inv