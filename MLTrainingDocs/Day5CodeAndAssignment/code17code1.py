# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:56:04 2018

@author: Anshu Pandey
"""

import tensorflow as tf
#tensor
x=tf.constant(0.5)
y=tf.constant(4.5)
#flow
z=x+y

sess=tf.Session()
fr=tf.summary.FileWriter('output')
fr.add_graph(tf.get_default_graph())
print(sess.run(z))
sess.close()

