# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:44:47 2021

@author: sydmo
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from openpyxl import load_workbook

# this line will print the directory that you should have your excel files in to
print(os.getcwd())

path_inputs = 'Yuma Data.xlsx'
sheet_name_setup = 'Sheet1'
inputs = pd.read_excel('Yuma Data.xlsx', 'Sheet1')
df = inputs.iloc[:, [0,27,7]]  # column/row counts starting at 0
df = df.sort_values(by=['Heat Units', 'Coliforms /100 ml'], ascending = True) # organizes data in ascending order
df = df.dropna() # drops all NaN values
df = df.reset_index(drop = True) # consolidates data points after NaN stripping
#df[(np.abs(stats.zscore('Coliforms /100 ml')) < 3)] # attempt at z-score FAILED
df.to_csv('Yuma.csv', index = False) # saves data to .csv file
