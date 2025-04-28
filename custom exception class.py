# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:43:11 2025

@author: test
"""

class customError(Exception):
    pass
try:
    raise customError("This is a custom exception!")
except customError as e:
    print(f"Caught an exception:{e}")