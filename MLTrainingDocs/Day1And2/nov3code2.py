# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:29:16 2018

@author: Anshu Pandey
"""

import numpy

x=[4,2,9]
y=[3,8,7]

x+y

a=numpy.array([7,8,6,3])
b=numpy.array([3,2,1,6])
a+b
a-b
a*b
a/b

c=numpy.array([[7,5,3,6],[1,4,9,6],[3,2,4,7]])
c
c.shape
c.size
c.min()
c.max()
c.mean()
c.min(axis=1)#row wise operation
c.min(axis=0)#columnwise operation

#creating arrays with numpy
x=numpy.arange(10)
x=numpy.arange(2,12)
x=numpy.arange(3,12,2)
x

x=numpy.linspace(1,10,21)
x
y=numpy.logspace(1,5,5,dtype='int32')
y
y=numpy.ones(6)
y=numpy.ones((2,3))
y
z=numpy.zeros((2,4))
z
#Random Numbers

numpy.random.rand(5)
numpy.random.seed(6)
numpy.random.randint(10,20,5)

#Linear Algebra using Numpy

#2x+y=11
#x-3y=-12

a=[[2,1],[1,-3]]
b=[[11],[-12]]
numpy.linalg.solve(a,b)

m=numpy.matrix([[4,7,3],[3,2,7],[1,5,8]])
m
numpy.linalg.inv(m)
numpy.linalg.det(m)
numpy.linalg.matrix_rank(m)
numpy.linalg.eig(m)

#basic mathematics

numpy.sin(45)
numpy.cos(45)
numpy.exp(45)
numpy.log10(45)
numpy.log(45)
numpy.sqrt(45)
numpy.square(45)




