import pandas as pd 
from pandas import Series,DataFrame
from sklearn.externals import joblib
import numpy as np

def test(test_data):
    print('----开始测试----')
    print(test_data)
    test_X = np.array(test_data)
    model_file = 'preT_ridge.pkl'
    reg = joblib.load(model_file)
    pre_y = reg.predict(test_X)
    print(pre_y)
    print('----测试完成----')

def begin(file_path):
    data = pd.read_csv(file_path)
    frame = DataFrame(data)
    test(frame)

if __name__ == '__main__':
    begin('test.csv')
