# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:44:47 2021

@author: sydmo
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# this line will print the directory that you should have your excel files in to
print(os.getcwd())

path_inputs = 'Yuma Data Only - Tamimi.xlsx'
sheet_name_setup = 'Sheet1'
inputs = pd.read_excel('Yuma Data Only - Tamimi.xlsx', 'Sheet1')

print(inputs.iloc[:, [0,7,27]]) # column/row counts starting at 0
