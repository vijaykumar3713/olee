# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:17:45 2024

@author: KJC Staff
"""

def get_matrix(rows,cols):
    """Function to get matrix input from the user"""
    matrix=[]
    print(f"Enter the elements of a {rows}x{cols} matrix, row by row:")
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row)!=cols:
            raise ValueError("Number of elements in the row does not match the specified columns.")
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Function to print matrix"""
    for row in matrix:
        print(' '.join(map(str, row)))
        
def add_matrices(A,B):
    if len(A)!= len(B) or len(A[0])!= len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return[[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A,B):
    if len(A)!= len(B) or len(A[0])!= len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return[[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A,B):
    if len(A[0])!= len(B):
        raise ValueError("Number of columns in A and B must be 2equal in number of rows in B.")
    return[[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose_matrix(A):
    return[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
2 
def main():
    try:
        rows_A= int(input("Enter number of rows for matrix A:"))
        cols_A= int(input("Enter number of columns for matrix A:"))
        A= get_matrix(rows_A,cols_A)
        rows_B= int(input("Enter number of rows for matrix B:"))
        cols_B= int(input("Enter number of columns for matrix B:"))
        B= get_matrix(rows_B,cols_B)
        print("\n Matrix A: ")
        print_matrix(A)
        print("\n Matrix B: ")
        print_matrix(B)
        if rows_A==rows_B and cols_A==cols_B:
            print("\n Addition of A and B: ")
            result_add= add_matrices(A, B)
            print_matrix(result_add)
            print("\n Subtraction of A and B: ")
            result_sub= subtract_matrices(A, B)
            print_matrix(result_sub)
        else:
            print("\n Matrices must have the same dimensions for addition and Subtraction")
        
        if cols_A== rows_B:
            print("\n Multiplication of A and B: ")
            result_mul= multiply_matrices(A, B)
            print_matrix(result_mul)
            
        else:
            print("\n Multiplicvation requires the number of columns in A to be equal to the number of rows in B.")
        print("\n Transpose of matrix A: ")
        result_transpose_A= transpose_matrix(A)
        print_matrix(result_transpose_A)     
        
        print("\n Transpose of matrix B: ")
        result_transpose_B= transpose_matrix(B)
        print_matrix(result_transpose_B)
        
    except ValueError as e:
        print(f"Error:{e}")


if __name__=="__main__":
    main()
        
            