import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.interpolate import spline
import xlrd
from sklearn.metrics import mean_squared_error

with xlrd.open_workbook("predictions.xlsx") as data:
     #data = xlrd.open_workbook('5minutes.xlsx')
     # sh = wb.sheet_by_name('sheet1')
     table = data.sheets()[0]
     nrows = table.nrows  # 行数
     ncols = table.ncols  # 列数
     #print(nrows, ncols)

     pre = np.array([])
     y = np.array([])
     for i in range(0, nrows):
          rowValues1 = table.row_values(i)[0]  # 某一行数据
          rowValues2 = table.row_values(i)[1]
          pre = np.append(pre, rowValues1)
          y = np.append(y, rowValues2)

x = np.array([])
for i in range(len(pre)):
     x = np.append(x, i)

# mse = mean_squared_error(y, pre)

# print(mse)

plt.figure(figsize=(12, 6))

plt.xlabel("time", fontsize=15)
plt.ylabel("prediction", fontsize=15)

plt.xlim(0, 500)
plt.ylim(1.17, 1.19)

# 曲线
l1 = plt.plot(x, y, color='blue', linewidth=0.5)
l2 = plt.plot(x, pre, color='red', linewidth=0.5)

# 标注
#plt.legend(loc='lower right')

# 图像边界
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 字体
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

# 小数
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%1.3f"))

# 科学计数法
"""formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))
ax.yaxis.set_major_formatter(formatter)"""

# 网格
plt.grid(True)
ax.xaxis.grid(True, color='grey', linestyle='--')
ax.yaxis.grid(True, color='grey', linestyle='--')

plt.show()
