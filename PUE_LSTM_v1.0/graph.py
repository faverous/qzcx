import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.interpolate import spline
import xlrd

with xlrd.open_workbook("total.xlsx") as data:
     #data = xlrd.open_workbook('5minutes.xlsx')
     # sh = wb.sheet_by_name('sheet1')
     table = data.sheets()[0]
     nrows = table.nrows  # 行数
     ncols = table.ncols  # 列数
     #print(nrows, ncols)

     l = np.array([])
     for i in range(0, nrows):
          rowValues = table.row_values(i)  # 某一行数据
          l = np.append(l, rowValues)

x = np.array([])
for i in range(len(l)):
     x = np.append(x, i)


plt.figure(figsize=(12, 6))

plt.xlabel("steps", fontsize=15)
plt.ylabel("total loss", fontsize=15)

plt.xlim(0, 200)
print(len(x))
# 曲线
l1 = plt.plot(x, l, color='blue', linewidth=0.5)

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
