# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
try:
    num =int(input("Enter a number:"))
    result = 10/ num
except ZeroDivisionError :
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input ! Please enter a number:")