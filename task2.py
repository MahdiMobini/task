import numpy as np


def calculate_xTx(X):
    n = X.shape[0]          

    x2 = 0.0
    x = 0.0
    sum_ones = 0.0
    for i in range(n):
        x2 += float(X[i][0] ** 2)
        x += float(X[i][0])
        sum_ones += 1.0

    XtX = [
        [x2, x],
        [x, sum_ones]
    ]
    
    print(f"\nTask 2 : X^T * X = ")
    for row in XtX:
        print(f"{row}")
    return XtX