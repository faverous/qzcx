import pandas as pd 
from pandas import Series,DataFrame
from sklearn.externals import joblib
import numpy as np

# test_data为dataframe格式数据
# 测试
def test(test_data):
    print('----开始测试----')
    print(test_data)
    test_X = np.array(test_data)
    model_file = 'preT_ridge.pkl'
    reg = joblib.load(model_file) # 加载模型
    pre_y = reg.predict(test_X)
    print(pre_y) #输出测试结果
    print('----测试完成----')

def begin(file_path):
    data = pd.read_excel(file_path) #读取数据
    frame = DataFrame(data)
    test(frame)

if __name__ == '__main__':
    begin('test_ridge_T3.xlsx')
