import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('datamini/relavent.csv')
X = np.array(data.ix[:,0])
Y = np.array(data.ix[:,1])
plt.figure(1)
plt.bar(range(len(X)),Y)
plt.show()