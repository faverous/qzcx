from sklearn import linear_model
import csv
import os
import numpy as np
import xlrd
from sklearn.externals import joblib

#调用岭回归模型 
clf = linear_model.Ridge (alpha = .9)
#载入训练数据集
inpath = "sz_pre_T3.xlsx"
data = xlrd.open_workbook(inpath)
table = data.sheets()[0] #获取第x张工作表
rows = table.nrows
cols = table.ncols
X = []
y = []
num = 1
test_X = []
test_y = []
print(rows)
for i in range(1,rows):
    # values = []
    row = table.row_values(i)
    if num < 4660:
        X.append(row[:-1])
        y.append(row[-1])
    else:
        test_X.append(row[:-1])
        test_y.append(row[-1])
    num = num + 1
arr_X = np.array(X)
arr_y = np.array(y)
test = np.array(test_X)
print(arr_y)
print("---开始训练---")
clf.fit(arr_X,arr_y)
joblib.dump(clf,'Pre_Tem_ridge.pkl')
print("---训练完成---")
print("---开始测试---")
clf1=joblib.load('Pre_Tem_ridge.pkl')
pre_y = clf1.predict(test)
print(test_y)
print(pre_y)
print("---测试完成---")