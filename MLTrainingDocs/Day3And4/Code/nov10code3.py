# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:31:49 2018

@author: Anshu Pandey
"""

import pandas
import matplotlib.pyplot as plt
import numpy

df=pandas.read_csv(r"F:\MLIoT\ML\dataset\Wholesale customers data.csv")

df2=df[['Fresh','Milk']]

from sklearn.cluster import KMeans
model=KMeans(n_clusters=3,
             random_state=5)
model.fit(df2)

model.cluster_centers_

plt.hist(model.labels_)

df2['cluster']=model.labels_

plt.figure(figsize=(8,5))
plt.scatter(x='Fresh',y='Milk',c='r',
            data=df2[df2['cluster']==0],
            label="Low Fresh Medium Milk")
plt.scatter(x='Fresh',y='Milk',c='g',
            data=df2[df2['cluster']==1],
            label="High Fresh High Milk")
plt.scatter(x='Fresh',y='Milk',c='b',
            data=df2[df2['cluster']==2],
            label="Medium Fresh Low Milk")
plt.legend()
plt.show()


df3=df[['Fresh','Milk','Grocery','Frozen']]


model2=KMeans(n_clusters=4,verbose=True,tol=1e-10)
model2.fit(df3)

model2.cluster_centers_

plt.hist(model2.labels_)


