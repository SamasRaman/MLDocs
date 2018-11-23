# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:18:45 2018

@author: Anshu Pandey
"""

import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
numpy.random.seed(6)
df=pandas.read_excel(r"F:\MLIoT\ML\dataset\CCPP (1)\CCPP\Folds5x2_pp.xlsx")

cor=df.corr()
plt.figure(figsize=(5,5))
sns.heatmap(cor,annot=True,cmap='coolwarm')
plt.show()

sns.pairplot(df)

y=df['PE']
x=df.drop(['PE'],axis=1)

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

#train the algorithm
model.fit(xtr,ytr)

ip=numpy.array([13.97,39.16,1016.05,84.6]).reshape(1,4)
model.predict(ip)

#performance analysis
ypred=model.predict(xts)
from sklearn import metrics
metrics.r2_score(yts,ypred)


from sklearn.externals import joblib
joblib.dump(model,'ccpp_model.pkl')


