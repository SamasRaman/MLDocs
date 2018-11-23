# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 10:45:37 2018

@author: Anshu Pandey
"""
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

df=pandas.read_csv(r"C:\Users\Roboindia\Desktop\Churn_Modelling.csv")
df.drop(['RowNumber','Surname','CustomerId'],
        axis=1,inplace=True)

x=df.drop(['Exited'],axis=1)
y=df['Exited']

from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()
x['Geography']=le1.fit_transform(x['Geography'])

le2=LabelEncoder()
x['Gender']=le2.fit_transform(x['Gender'])

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.2)
#pipeline of operations

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.tree import DecisionTreeClassifier

fmodel=Pipeline([('ohe',OneHotEncoder(categorical_features=[1],
                                      sparse=False)),
                 ('sc',StandardScaler()),
                 ('model',DecisionTreeClassifier(max_depth=10))])

fmodel.fit(xtr,ytr)
