
from task1 import read_and_display_data
from task2 import calculate_xTx
from task3 import cal_det2to2
from task4 import cal_inverse
from task5 import cal_xTy
from task6 import cal_beta
from task7 import cal_new_y


def main():
    file_path = "Input data.xlsx"
    
    x , y = read_and_display_data(file_path)
    XtX = calculate_xTx(x)
    det = cal_det2to2(XtX)
    inv = cal_inverse(XtX , det)
    xTy = cal_xTy(x, y)
    beta = cal_beta(inv, xTy)
    new_y = cal_new_y(beta, x)
    print("\nAll tasks completed!")


if __name__ == "__main__":
    main()