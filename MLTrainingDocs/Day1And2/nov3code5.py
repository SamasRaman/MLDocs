# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:57:57 2018

@author: Anshu Pandey
"""

import numpy
import matplotlib.pyplot as plt

x=numpy.arange(-10,10,0.5)
y=numpy.sin(x)

plt.plot(x,y)
plt.show()

plt.scatter(x,y)
plt.show()

z=numpy.exp(0.2*x)

plt.figure(figsize=(8,4))
plt.plot(x,y,'r',label='sin(x)')
plt.plot(x,z,'g',label='exp(x)')
plt.title('sin v/s exp')
plt.xlabel('value of x')
plt.ylabel('value of y')
plt.legend()
plt.show()

x=[45,66,23,85]
lb=['BLR','DEL','CCU','BOM']
plt.pie(x,labels=lb)
plt.show()

temp=[24,25,26,23,24,26,35,25,24,26,35,24,25,26,25,28]

plt.hist(temp)
plt.show()


