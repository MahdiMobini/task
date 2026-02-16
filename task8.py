import matplotlib.pyplot as plt

def cal_plot(y_real, y_pred):
    """
    Plots real vs predicted values for comparison.
    """
    plt.figure(figsize=(10, 6))
    
    plt.scatter(range(len(y_real)), y_real, color='blue', label='Real Data')
    plt.plot(range(len(y_pred)), y_pred, color='red', label='Predicted Line')
    
    plt.title('Comparison: Real vs Predicted Gold Prices')
    plt.xlabel('Sample Index')
    plt.ylabel('Price (Toman)')

    
    print("\nTask 8 : Plotting the results...")
    plt.show()
