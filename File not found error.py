# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:38:13 2025

@author: test
"""

try:
    file = open("data.test", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error : File not found")