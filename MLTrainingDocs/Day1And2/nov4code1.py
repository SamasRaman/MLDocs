# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:35:52 2018

@author: Anshu Pandey
"""
import theano
import numpy
x=theano.tensor.fvector('x')
y=theano.tensor.fvector('y')
m=theano.shared(0.5,'m')
c=theano.shared(0.9,'c')
yhat=m*x+c
#cost function
cost=theano.tensor.mean(theano.tensor.sqr(y-yhat))/2
#Gradient Descent ALgorithm
LR=0.1
gradm=theano.tensor.grad(cost,m)
gradc=theano.tensor.grad(cost,c)
mn=m-LR*gradm
cn=c-LR*gradc

train=theano.function([x,y],cost,updates=[(m,mn),(c,cn)])
#data
area=[1.2,1.8,2.4,5.6,3.4,6.8,4.3,5.2,2.6,2.8]
price=[180,210,230,480,360,720,540,490,310,260]
area=numpy.array(area).astype('float32')
price=numpy.array(price).astype('float32')

predict=theano.function([x],yhat)
pred_price1=predict(area)
for i in range(1000):
    cost_val=train(area,price)
    print(cost_val)
pred_price2=predict(area)    
print(m.get_value())
print(c.get_value())

import matplotlib.pyplot as plt
plt.scatter(area,price)
plt.plot(area,pred_price1,'r')
plt.plot(area,pred_price2,'g')
plt.show()
