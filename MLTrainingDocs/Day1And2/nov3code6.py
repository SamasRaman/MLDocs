# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:16:36 2018

@author: Anshu Pandey
"""

import pandas
import matplotlib.pyplot as plt
import seaborn as sns

data=pandas.read_csv(r"C:\Users\Roboindia\Desktop\Churn_Modelling.csv")

data.drop(['RowNumber','Surname','CustomerId'],
          axis=1,inplace=True)

plt.figure(figsize=(8,4))
sns.distplot(data['CreditScore'][data['Exited']==0])
sns.distplot(data['CreditScore'][data['Exited']==1])
plt.legend(['0','1'])
plt.show()

plt.figure(figsize=(8,4))
sns.distplot(data['Age'][data['Exited']==0])
sns.distplot(data['Age'][data['Exited']==1])
plt.legend(['0','1'])
plt.show()


plt.figure(figsize=(8,3))
sns.countplot(data['Geography'])
plt.show()
plt.figure(figsize=(8,3))
sns.countplot(data['Geography'][data['Exited']==1])
plt.show()

plt.figure(figsize=(8,3))
sns.countplot(data['Gender'])
plt.show()
plt.figure(figsize=(8,3))
sns.countplot(data['Gender'][data['Exited']==1])
plt.show()


cor=data.corr()
plt.figure(figsize=(10,6))
sns.heatmap(cor,annot=True,cmap='coolwarm')
plt.show()


