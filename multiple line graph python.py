# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:21:05 2025

@author: test
"""

import matplotlib.pyplot as plt
years = [2018,2019,2020,2021,2022]
product_A = [12,13,15,10,16]
product_B = [125,137,135,145,155]
product_C = [20,35,38,40,50]
product_D = [110,120,150,160,170]
product_E = [100,125,130,180,160]
plt.plot(years, product_A, label="Product A", marker='o', linestyle='-', color='blue')
plt.plot(years, product_B, label="Product B", marker='s', linestyle='--', color='green')
plt.plot(years, product_C, label="Product C", marker='^', linestyle='-', color='yellow')
plt.plot(years, product_D, label="Product D", marker='x', linestyle=':', color='pink')
plt.plot(years, product_E, label="Product E", marker='d', linestyle='--', color='brown')
plt.xlabel('years')
plt.ylabel('sales')
plt.title('sales trend of 5 products')
plt.grid(True)
plt.legend()
plt.show()               