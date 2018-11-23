# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:21:53 2018

@author: Anshu Pandey
"""

import pandas
data=pandas.read_csv(r"D:\AI\QG\B2\datawh.csv")

data=pandas.read_csv(r"D:\AI\QG\B2\datanh.csv",
                     header=None)
data.columns=['temp','hum','pres','air']

data=pandas.read_csv(r"D:\AI\QG\B2\datawh_missing.csv",
                     na_values=['.','?'])
#check for missing values
data.isnull().sum()

#dropping the row/observation where more than 3 missing values
data.dropna(thresh=3,inplace=True)
#replacing the missing values of temperature by mean
x=data['Temperature'].mean()
data['Temperature'].fillna(x,inplace=True)

data.fillna(data.median(),inplace=True)
