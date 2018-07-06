from sklearn import linear_model
import numpy as np
import xlrd
from sklearn.externals import joblib

# 读取excel文件
def read_excel(inpath):
    print("----读取文件----")
    data = xlrd.open_workbook(inpath)
    table = data.sheets()[0] #获取第0张工作表
    rows = table.nrows
    cols = table.ncols
    X = []
    y = []
    for i in range(1, rows): #从第1行开始，忽略列名
        row = table.row_values(i)
        X.append(row[:-1])
        y.append(row[-1])
    print("----读取完成----")
    return X, y

# 岭回归训练模型
def train_ridge(excel_file, model_file = 'preT_ridge.pkl'):
    train_X, train_y = read_excel(excel_file)
    print("----开始训练----")
    reg = linear_model.Ridge (alpha = .9)
    reg.fit(train_X, train_y)
    joblib.dump(reg, model_file)
    print("----训练完成----")

# 测试，测试数据需要有温度标签填充
def test_ridge(excel_file, model_file = 'preT_ridge.pkl'):
    test_X, test_y = read_excel(excel_file)
    print('----开始测试----')
    reg = joblib.load(model_file)
    pre_y = reg.predict(test_X)
    print(test_y)
    print(pre_y)
    print('----测试完成----')

# if __name__ == '__main__':
#     excel_file = "test_ridge_T3.xlsx"
#     # train_ridge(excel_file)
#     test_ridge(excel_file)
