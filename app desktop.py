# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:43:11 2025

@author: test
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('My First App Desktop')
window.setGeometry(200, 200, 380, 160)

label = QLabel('First App' , parent=window)
window.show()
sys.exit(app.exec_())