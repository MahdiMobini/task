# the target is calculating β = (XᵀX)⁻¹ × Xᵀy

def cal_beta(XtX_inv, xTy):

    beta = []    
    for i in range(2):
        beta.append(sum(float(XtX_inv[i][k] * xTy[k][0]) for k in range(2)))

    print(f"\nTask 6 : Beta = \n{beta}\n")
    
    return beta

    