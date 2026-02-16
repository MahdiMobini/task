# calculate y with beta and x
def cal_new_y(beta, x):
    new_y = []
    for i in range(len(x)):
        new_y.append(beta[0] * x[i] + beta[1])
    
    print(f"\nTask 7 : Predicted y values = \n")
    for row in new_y:
        print(row)
    return new_y