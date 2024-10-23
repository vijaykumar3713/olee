# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:46:33 2024

@author: KJC Staff
"""
def write_to_file(filename):
    with open(filename,'w') as file:
        print("Enter text to write in the file. Type 'exit' on a new line to finish.")
        while True:
            line=input()
            if line.lower()=='exit':
                break
            file.write(line+'\n')
            print(f"Data written to : {filename}")
            
def read_from_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print("\nFile Content: ")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename}  does not exist.")
        
def append_to_file(filename):
    with open(filename,'a') as file:
        print("Enter text to append to the file. Type 'exit' on a new line to finish.")
        while True:
            line=input()
            if line.lower()=='exit':
                break
            file.write(line+'\n')
            print(f"Data appended to : {filename}")
            
def read_lines_from_file(filename):
    try:
        with open(filename,'r') as file:
            lines= file.readlines()
            print("\n Lines in File: ")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        
def main():
    while True:
        print("1. Write to a file")
        print("2. Read from a file.")
        print("3. Append to a file.")
        print("4. Read lines from a file")
        print("5. Exit")
        choice= input("Enter your choice(1-5): " )
        if choice=='1':
            filename=input("Enter the filename to write to:")
            write_to_file(filename)
        elif choice=='2':
            filename=input("Enter the filename to read from:")
            read_from_file(filename)
        elif choice=='3':
            filename=input("Enter the filename to append to:")
            append_to_file(filename)
            
            
            
            
            
            
        elif choice=='4':
            filename=input("Enter the filename to read  the lines from:")
            read_lines_from_file(filename)
        elif choice=='5':
            print("EXITING....")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 5.")
            
if __name__=="__main__":
    main()
        
        
        
