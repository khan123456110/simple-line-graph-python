# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:21:05 2025

@author: test
"""

import matplotlib.pyplot as plt
import numpy as np
x = [5,6,8,9]
y = [20,40,60,50]
size = [30, 40, 80, 90]
plt.scatter(x ,y, s=size, alpha=0.5, color='purple')
plt.title("bubble chart")   
plt.xlabel("X")
plt.ylabel("Y") 
plt.show()