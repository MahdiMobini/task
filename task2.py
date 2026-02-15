import numpy as np


def calculate_xTx(X):
    n = X.shape[0]          # تعداد ردیف‌ها = 10
    XtX = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(2):          # فقط ۲ ستون داریم
                s += X[i, k] * X[j, k]
            XtX[i, j] = s
    print(f"Task 3 : X^T * X = \n{XtX}\n")
    return XtX