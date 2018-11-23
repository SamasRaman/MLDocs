# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:20:29 2018

@author: Anshu Pandey
"""

import numpy
import matplotlib.pyplot as plt

x=numpy.arange(-50,50)

plt.plot(x)
plt.show()


y=1/(1+numpy.exp(-1*x))

plt.plot(x,y)
plt.show()
