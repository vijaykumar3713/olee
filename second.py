# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:10:29 2024

@author: KJC Staff
"""

def dictionary_operations():
    d={}
    while True:
        print("\n Dictionary Operataions Manu: ")
        print("1.Add key-value pair")
        print("2.Remove Key")
        print("3. Display Dictionary")
        print("4. Search for Key:")
        print("5. Exit")
        choice= input("Enter your choice: ")
        if choice=='1':
            key= input("Enter the key: ")
            value= input("Enter the value: ")
            d[key]= value
            print(f"Added: {{'{key}' : '{value}'}}")
        elif choice=='2':
             key= input("Enter the key to remove: ")
             if key in d:
                 del d[key]
                 print(f"Removed Key:{key}")
             else:
                 print("Key not found")
        elif choice=='3':
            print("Current dictionary contents: ")
            for k,v in d.items():
                print(f"{k}:{v}")
        elif choice=='4':
            key= input("Enter the key to search: ")
            if key in d:
                print(f"Key:'{key}' found with value: {d[key]}")
            else:
                print("Key not found")
        elif choice=='5':
                 break
        else:
             print("Invalid choice. Please try again.")
                
def set_operations():
    s= set()
    while True:
        print("\n Set Operataions Menu: ")
        print("1.Add element")
        print("2.Remove element")
        print("3. Display Set")
        print("4. Check if element exists")
        print("5. Exit")
        choice= input("Enter your choice: ")
        if choice=='1':
            element= input("Enter the element to add: ")
            s.add(element)
            print(f"Added element: {element}")
        elif choice=='2':
                element= input("Enter the element to remove: ")
                if element in s:
                    s.remove(element)
                    print(f"Removed Element:{element}")
                else:
                     print("Element not found")
        elif choice=='3':
             print("Current set contents: ")
             print(s)
        elif choice=='4':
             element= input("Enter the element to check: ")
             if element in s:
                 print(f"Element:'{element}' exists in the set")
             else:
                 print("Element not found")
        elif choice=='5':
             break
        else:
             print("Invalid choice. Please try again.")
                     
        
def main():
    while True:
        print("\n Main menu:")
        print("1.Dictionary operations")
        print("2.Set operations")
        print("3.Exit")
        choice= input("Enter your choice: ")
        if choice=='1':
            dictionary_operations()
            choice= input("Enter your choice: ")
        elif choice=='2':
            set_operations()
        elif choice=='3':
            print("EXITING....")
            break
        else:
            print("Invalid choice. Please try again")
            
if __name__=="__main__":
    main()
        
        
    
                
        