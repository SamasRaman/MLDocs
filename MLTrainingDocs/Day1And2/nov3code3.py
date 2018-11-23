# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:27:01 2018

@author: Anshu Pandey
"""

import numpy
import pandas

data=numpy.random.randint(40,80,(20,5))
col=['M1','M2','M3','M4','M5']
rows=pandas.date_range('20181025',periods=20)

df=pandas.DataFrame(data,index=rows,columns=col)

df['M3']
df['M3']['2018-11-05':'2018-11-08']

df['2018-11-05':'2018-11-08']

df['M3'][df['M3']>70]
df[['M3','M4']]
#Data of M3 and M4 where M3>70
df[['M3','M4']][df['M3']>70]
#Data of M3 and M4 where M3>70 and M4>70
df[['M3','M4']][df['M3']>70][df['M4']>70]
df[['M3','M4']][(df['M3']>70) & (df['M4']>70)]

#data of M3 and M4 where M3>70 OR m4>70
df[['M3','M4']][(df['M3']>70)|(df['M4']>70)]

#statistical summary
summary=df.describe()
#stats
df['M3'].min()
df['M3'].max()
df['M3'].mean()
df['M3'].median()
df['M3'].mode()
df['M3'].var()
df['M3'].std()
df['M3'].skew()
df['M3'].kurt()

#export data
df.to_excel('machines.xlsx')

