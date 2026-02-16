def cal_xTy(X, Y):    
    n = len(X)

    sum_x_y = 0.0
    sum_y = 0.0
    sum_x = 0.0
    sum_ones = 0.0
    for i in range(n):
        xi = float(X[i][0])
        yi = float(Y[i][0])   

        sum_x_y += xi * yi
        sum_y += yi
        sum_x += xi
        sum_ones += 1.0

    XTy = [
        [sum_x_y],
        [sum_y] 
    ]

    print("Task 5 : X^T y =")
    for row in XTy:
        print(row)

    return XTy