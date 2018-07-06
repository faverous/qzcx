import xlrd
import numpy as np

ceshi = xlrd.open_workbook("train.xlsx")
table = ceshi.sheets()[0]
nrows = table.nrows
ncols = table.ncols

x = []
X = []
#Y = []
for i in range(nrows - 10 + 1):
    for j in range(10):
        rowValues1 = table.row_values(i + j)[:]
        x.append(rowValues1)
    X.append(x)
    x = []
    #Y.append(table.row_values(i + 16 - 1)[-1])


# print(X)
# print(Y)

arrX = np.array(X)
#arrY = np.array(Y)
x_batch = arrX[0:0 + 10, :, :-1]
y_batch = arrX[0:0 + 10, -1, -1]

print(arrX)
print(x_batch)
print(y_batch)
# print(arrY)
