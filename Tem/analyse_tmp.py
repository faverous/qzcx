'''
数据分析，观察机房温度变化，冷暖通道差值变化
'''

import pandas as pd 
import numpy as np 
from pandas import DataFrame
import xlrd
# import matplotlib.pyplot as plt 

data = xlrd.open_workbook('Tem/机房温湿度.xlsx')
table = data.sheets()[0]
rows = table.nrows
X = []
Y = []
Z = []
j = 1
for i in range(3,rows):
    row = table.row_values(i)
    if row[1] and row[3] and row[5] and row[7] and row[9] and row[11] and row[13] and row[15] and row[17] and row[19] and row[21] and row[25] and row[27]:
        leng = (row[1]+row[3]+row[5]+row[7]+row[19]+row[21]+row[25]+row[27])/8
        hot = (row[9]+row[11]+row[13]+row[15]+row[17])/5
        X.append(leng)
        Y.append(hot)
        Z.append(hot - leng)
        j = j+1
print(j)
print('读取完成')
# ans = np.array(X)
# ansy = np.array(Y)
# plt.figure(1)
# plt.bar(ansy,ans)
# plt.show()
print('----冷风----')
print(max(X))
print(min(X))
print(max(X)-min(X))
print('----暖风----')
print(max(Y))
print(min(Y))
print(max(Y)-min(Y))
print('----温差----')
print(max(Z))
print(min(Z))
