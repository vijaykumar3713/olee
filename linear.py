# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:56:28 2024

@author: KJC Staff
"""

import matplotlib.pyplot as plt

def get_data():
    """Function to get matrix input from the user"""
    print("Enter the elements of X and Y:")
    x = list(map(float, input("X values (space-separated): ").split()))
    y = list(map(float, input("Y values (space-separated): ").split()))
    
    if len(x) != len(y):
        raise ValueError("The number of X values must match the number of Y values.")
    
    mean_x = mean(x)
    mean_y = mean(y)
    
    print("Mean of X:", mean_x)
    print("Mean of Y:", mean_y)
    
    xi_minus_xbar = [xi - mean_x for xi in x]
    yi_minus_ybar = [yi - mean_y for yi in y]
    
    print("xi - X':", xi_minus_xbar)
    print("yi - Y':", yi_minus_ybar)
    
    xi_minus_xbar_multiply_yi_minus_ybar = [xi * yi for xi, yi in zip(xi_minus_xbar, yi_minus_ybar)]
    sum_xi_minus_xbar_multiply_yi_minus_ybar = sum(xi_minus_xbar_multiply_yi_minus_ybar)
    
    print("(xi - X')(yi - Y'):", xi_minus_xbar_multiply_yi_minus_ybar)
    print("Sum(xi - X')(yi - Y'):", sum_xi_minus_xbar_multiply_yi_minus_ybar)
    
    xi_minus_xbar_squared = [xi ** 2 for xi in xi_minus_xbar]
    sum_xi_minus_xbar_squared = sum(xi_minus_xbar_squared)
    
    print("(xi - X')^2:", xi_minus_xbar_squared)
    print("Sum(xi - X')^2:", sum_xi_minus_xbar_squared)
    
    if sum_xi_minus_xbar_squared == 0:
        raise ValueError("Variance of X values is zero, cannot compute slope.")
    
    slope_value = compute_slope(sum_xi_minus_xbar_multiply_yi_minus_ybar, sum_xi_minus_xbar_squared)
    print("Slope:", slope_value)
    
    y_intercept = compute_y_intercept(mean_y, slope_value, mean_x)
    print("Y-Intercept:", y_intercept)

    print("Equation of the line:")
    new_y = [straight_line(slope_value, xi, y_intercept) for xi in x]
    print(new_y)
    
    plot_graph(x, new_y, x, y)
    
    return x, y

def straight_line(m, x, b):
    return m * x + b

def compute_y_intercept(y, m, x):
    return y - (m * x)

def compute_slope(a, b):
    return a / b

def mean(values):
    return sum(values) / len(values)

def print_matrix(x, y):
    for xi, yi in zip(x, y):
        print(f"{xi} {yi}")

def plot_graph(x_values, y_values_line, original_x, original_y):
    plt.plot(x_values, y_values_line, label='y = mx + b', color='blue')  # Plot the line
    plt.scatter(original_x, original_y, color='red', label='Data Points')  # Plot the data points
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Plot of Straight Line')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    try:
        x, y = get_data()
        print("\nX and Y data elements:")
        print_matrix(x, y)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
