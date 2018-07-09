import pandas as pd
import csv
import numpy as np
import xlsxwriter

# def out_excel(tmplist, outpath):
#     print("----开始写入数据----")
#     pos_data = xlsxwriter.Workbook(outpath)
#     worksheet = pos_data.add_worksheet()
#     # style = xlwt.XFStyle()
#     # style.num_format_str = "[$-10804]0.00"
#     rows_pos = len(tmplist)
#     col_pos = len(tmplist[0])
#     print(rows_pos)
#     for i in range(rows_pos):
#         for j in range(col_pos):
#             worksheet.write(i, j, tmplist[i][j])
#         worksheet.write(i, j, tmplist[i][j])
#     pos_data.close()
#     print("----写入完成----")

data = pd.read_csv("/Users/mj/Desktop/预测机房温度湿度/clean_data.csv")

nan_num_per_col = list(data.shape[0] - data.count(axis=0))
print(nan_num_per_col)

many_nan_cols_index = list()
several_nan_cols_index = list() # nan number less than 2
for i in range(len(nan_num_per_col)):
    if nan_num_per_col[i] >2:
        many_nan_cols_index.append(i)
    elif nan_num_per_col[i] <=2 and nan_num_per_col[i] > 0:
        several_nan_cols_index.append(i)
        
print(many_nan_cols_index)
print(several_nan_cols_index)

# 室外湿度2 填充这一条为上一条+0.25
# 变化小的：E_实际冷冻水温度设定，A路_总供水温度_1，总_A路回水压力_1，总_B路供水压力_1
# 总_B路回水压力_1，总_A路供水压力_1，一次环管供水A压力1，一次环管供水A压力2
# 一次环管供水B压力1，A路_总供水温度_2，一次环管供水B压力2，A路_总回水温度_1，A路_总回水温度_2
# B路_总供水温度1，B路_总供水温度_2，B路_总回水温度_1，B路_总回水温度_2，二期变压器损耗
# 二期UPS损耗
# 填平均值
# label 暖通PUE_30分钟 变化小，也填平均值
# drop 这一列：二次泵功率

# fill incremently
original_cols = data['室外湿度2'].tolist()
for i in range(len(original_cols)):
    if np.isnan(original_cols[i]):
        original_cols[i] = original_cols[i-1]
        
data['室外湿度2'] = pd.Series(original_cols)

# # drop whole columns
data = data.drop(['二次泵功率'],axis = 1)

# fill average
column_name = list(data.columns.tolist())
other_col_index = list(set(list(many_nan_cols_index)).difference([column_name.index('室外湿度2')]))
data = data.fillna(data.mean())

 
print(list(data.shape[0] - data.count(axis=0)))

y = data['暖通PUE_30分钟']

data = data.drop(['时间','暖通PUE','暖通PUE_30分钟'],axis=1)

ground_cols = ['A_电机电流百分比_%','B_电机电流百分比_%','C_电机电流百分比_%',
'D_电机电流百分比_%','E_电机电流百分比_%','F_电机电流百分比_%','B套主机功率','C套主机功率', 'A套主机功率',
              'E套主机功率','F套主机功率','D套主机功率','二期_冷冻系统功率','二期_PUE','二期_输入总功率（KW）']
data = data.drop(ground_cols,axis=1)
data.to_csv("clean_data2.csv")


# X_train,X_test,y_train,y_test = train_test_split(data, y, test_size=0.1,random_state=2)
# X_train = X_train.values
# y_train = y_train.values.reshape(-1,1)
# X_test = X_test.values
# y_test = y_test.values.reshape(-1,1)
