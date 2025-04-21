# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:21:05 2025

@author: test
"""

import matplotlib.pyplot as plt
data=[19,15,30,20,30,50,60,90,30,40,70,10,30]
plt.hist(data , bins=5,color='pink', edgecolour='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram chart(list data) ')
plt.show()               