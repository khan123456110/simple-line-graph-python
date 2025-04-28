# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:29:14 2025

@author: test
"""

number = [10, 20, 30]
try:
    index = int(input("Enter index (0-2):"))
    print("Value:", number[index])
except IndexError :
    print("Error: index out of range!")