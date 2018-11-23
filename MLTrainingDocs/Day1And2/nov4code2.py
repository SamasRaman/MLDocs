# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:37:01 2018

@author: Anshu Pandey
"""

import numpy
import matplotlib.pyplot as plt
area=[1.2,1.8,2.4,5.6,3.4,6.8,4.3,5.2,2.6,2.8]
price=[180,210,230,480,360,720,540,490,310,260]
area=numpy.array(area).reshape(10,1)
price=numpy.array(price)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
#train the algorithm
model.fit(area,price)

model.coef_
model.intercept_
ypred=model.predict(area)
plt.scatter(area,price)
plt.plot(area,ypred)
plt.show()