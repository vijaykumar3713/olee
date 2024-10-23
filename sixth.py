# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:32:32 2024

@author: KJC Staff
"""

import pandas as pd

# Initialize an empty DataFrame
columns = ['ID', 'name', 'age', 'grade']
students_df = pd.DataFrame(columns=columns)

def display_menu():
    print("\nMenu:")
    print("1. Add student")
    print("2. View all students") 
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

def add_student():
    global students_df
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    new_student = pd.DataFrame([[id, name, age, grade]], columns=columns)
    students_df = pd.concat([students_df, new_student], ignore_index=True)
    print(f"Student {name} added successfully!")

def view_students():
    global students_df
    if students_df.empty:
        print("No students to display.")
    else:
        print("\nStudent details:")
        print(students_df)

def update_student():
    global students_df
    id = input("Enter student ID to update: ")
    if id in students_df['ID'].values:
        name = input("Enter new student name: ")
        age = input("Enter new student age: ")
        grade = input("Enter new student grade: ")
        students_df.loc[students_df['ID'] == id, ['name', 'age', 'grade']] = [name, age, grade]
        print(f"Student with ID {id} updated successfully!")
    else:
        print("Student ID not found.")

def delete_student():
    global students_df
    id = input("Enter student ID to delete: ")
    if id in students_df['ID'].values:
        students_df = students_df[students_df['ID'] != id]
        print(f"Student with ID {id} deleted successfully!")
    else:
        print("Student ID not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
