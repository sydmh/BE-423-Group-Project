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
df = df.sort_values(by=['Heat Units', 'Coliforms /100 ml'], ascending = True)
df = df.dropna()
df = df.reset_index(drop = True)
df.to_csv('Yuma.csv', index = False)

tC, Clmbda = stats.boxcox(df['Coliforms /100 ml'])
plt.hist(tC)
plt.xlabel('Transformed Coliform Concentration'), plt.ylabel('Frequency')
print(Clmbda)
df['Coliforms /100 ml'] = tC
h0 = df['Heat Units']
df.to_csv('Yuma.csv', index = False)

slope, intercept, r_value, p_value, std_err = stats.linregress(h0,tC)
plt.figure(2)
plt.plot(h0, tC, 'bo', tC, intercept+slope*tC, 'r-')
plt.xlabel('h0'); plt.ylabel('C')
plt.legend(['data', 'regression line'], loc='upper left')
filestem = 'growth1_%dsteps' % 5
plt.savefig('%spng' % filestem); plt.savefig('%s.pdf' % filestem)
print('slope = ', slope, 'intercept = ', intercept, 'R value = ', r_value)
