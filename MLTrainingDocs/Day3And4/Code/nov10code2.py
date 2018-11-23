# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:31:26 2018

@author: Anshu Pandey
"""

import pandas
import numpy
import matplotlib.pyplot as plt
path=r"https://archive.ics.uci.edu/ml/machine-learning-databases/semeion/semeion.data"
df=pandas.read_csv(path,header=None,sep=" ")
print(df.shape)
#as the last columns in non relevant one, lets drop it
df=df.iloc[:,:-1]
print(df.shape)

#spearating the first 256 cols as pixel values and
#last 10 cols as class values
img=numpy.array(df.iloc[:,0:256])
labels=numpy.array(df.iloc[:,256:266])
print(img.shape)
print(labels.shape)

plt.imshow(img[88].reshape(16,16),cmap='gray')
plt.show()
labels[88]

labels=labels.tolist()
lb=[]
for i in labels:
    lb.append(i.index(1))

lb=numpy.array(lb)

plt.imshow(img[88].reshape(16,16),cmap='gray')
plt.show()
lb[88]

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(img,lb,test_size=0.2)

from sklearn.svm import SVC
model=SVC(C=5,gamma=0.015)
#train the model with trainig dataset
model.fit(xtr,ytr)
#check the accuracy of the model
print(model.score(xtr,ytr))
print(model.score(xts,yts))

plt.imshow(xts[60].reshape(16,16),cmap='gray')
plt.show()

model.predict(xts[60].reshape(1,256))

import cv2
img=cv2.imread(r"D:\AI\QG\B2\img.png",0)
plt.imshow(img,cmap='gray')
plt.show()
model.predict(img.reshape(1,256))


#########################################
from sklearn import ensemble
model=ensemble.RandomForestClassifier(n_estimators=10)
model.fit(xtr,ytr)

model.score(xtr,ytr)
model.score(xts,yts)



