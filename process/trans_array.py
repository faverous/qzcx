# --coding:utf-8--
'''
将原始数据进行整理，保留所需数据并生成excel文件
'''

import numpy as np 
import xlrd
import xlsxwriter

l = [[1,2], [4,3], [2,5]]
print(l)
l1 = np.array(l).T
print (l1)
for i in range(len(l1)):
    print (sorted(l1[i])[-1])