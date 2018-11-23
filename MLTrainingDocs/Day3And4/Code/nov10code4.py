# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:55:57 2018

@author: Anshu Pandey
"""

import numpy
import matplotlib.pyplot as plt
x=numpy.random.randint(20,50,15)
y=0.9*numpy.random.randint(0,8,15)+0.8*x

plt.scatter(x,y)
plt.show()

data=numpy.concatenate(([x],[y]))
data=data.T
data.shape

from sklearn.decomposition import pca
pc=pca.PCA(n_components=1)

data2=pc.fit_transform(data)
data2.shape

pc.explained_variance_ratio_


