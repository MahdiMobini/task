# the target is calculating β = (XᵀX)⁻¹ × Xᵀy

def cal_beta(XtX_inv, xTy):

    beta = [[], []]    
    for i in range(2):
        for j in range(1):
            beta[i].append(sum(float(XtX_inv[i][k] * xTy[k][j]) for k in range(2)))

    print(f"\nTask 6 : Beta = \n{beta}\n")

    