# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:16:29 2024

@author: KJC Staff
"""
import re

def validate_email(email):
    pattern= r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None


def validate_phone_number(phone_number):
    pattern= r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern,phone_number) is not None

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None

def main():
    print("Welcome to the user validateion program.")
    email= input("Enter your email address: ")
    if validate_email(email):
        print("Email is valid.")
    else:
        print("Invalid Email.")
    
    phone_number= input("Enter your phone number: ")
    if validate_phone_number(phone_number):
        print("phone number is valid.")
    else:
        print("Invalid phone number.")
    
    password = input("Enter your password: ")
    if validate_password(password):
       print("Password is valid")
    else:
       print("Invalid password. Make sure it has at least 8 characters, one uppercase letter, one lowercase letter, and one digit") 
if __name__=="__main__":
    main()
