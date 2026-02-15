import pandas as pd
import numpy as np

def read_and_display_data(file_path):

    print("Task 1: Reading from Excel")
    
    df = pd.read_excel(file_path)
    

    x_values = df["قیمت ارز (تومان)"].values
    X = np.array([[int(i) , 1] for i in x_values])

    
    y_values = df["قیمت طلا (تومان)"].values
    Y = np.array([[int(i) , 1] for i in y_values])


 
    print("x:\n" , X)
    print("\nY :\n" , Y)
    return X , Y





