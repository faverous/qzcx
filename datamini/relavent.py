'''数据相关性分析'''
import pandas as pd 

# csv_path = 'datamini/clean_data.csv'
# data = pd.read_csv(csv_path,index_col=u'时间')
# ans = data.corr()[u'暖通PUE']
# ans.to_csv('relavent.csv')
# print(data.corr()[u'暖通PUE'])
csv_path = 'datamini/relavent.csv'
data = pd.read_csv(csv_path,usecols=[1])
data.to_csv('ans.csv')