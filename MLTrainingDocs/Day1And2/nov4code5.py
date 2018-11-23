# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:30:58 2018

@author: Anshu Pandey
"""

import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

df=pandas.read_csv(r"C:\Users\Roboindia\Desktop\Churn_Modelling.csv")
df.drop(['RowNumber','Surname','CustomerId'],
        axis=1,inplace=True)

cor=df.corr()
plt.figure(figsize=(10,12))
sns.heatmap(cor,annot=True,cmap='coolwarm')
plt.show()

x=df.drop(['Exited'],axis=1)
y=df['Exited']

from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
x['Geography']=le1.fit_transform(x['Geography'])

le2=LabelEncoder()
x['Gender']=le2.fit_transform(x['Gender'])

from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[1])
x=ohe.fit_transform(x).toarray()

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)
from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.2)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
numpy.random.seed(6)
#train the model
model.fit(xtr,ytr)
#Performance Analysis
ypred=model.predict(xts)
from sklearn import metrics
metrics.accuracy_score(yts,ypred)

metrics.recall_score(yts,ypred)

cm=metrics.confusion_matrix(yts,ypred)

#######################################################

from sklearn.tree import DecisionTreeClassifier
model2=DecisionTreeClassifier(max_depth=10,
                              min_samples_leaf=6,
                              min_samples_split=20)

#train the algorithm
model2.fit(xtr,ytr)

ypred2=model2.predict(xts)
metrics.accuracy_score(yts,ypred2)
model2.score(xts,yts)
model2.score(xtr,ytr)



metrics.recall_score(yts,ypred2)













