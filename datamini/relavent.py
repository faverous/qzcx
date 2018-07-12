'''数据相关性分析'''
import pandas as pd 

csv_path = 'datamini/clean_data.csv'
data = pd.read_csv(csv_path,index_col=u'时间')
ans = data.corr()[u'暖通PUE']
ans.to_csv('relavent.csv')
print(data.corr()[u'暖通PUE'])