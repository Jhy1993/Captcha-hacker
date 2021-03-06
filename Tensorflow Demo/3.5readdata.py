# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 22:21:00 2016

@author: Jhy1993
Github: https://github.com/Jhy1993

README:
TensorFlow程序读取数据一共有3种方法:
供给数据(Feeding)： 在TensorFlow程序运行的每一步， 让Python代码来供给数据。
从文件读取数据： 在TensorFlow图的起始， 让一个输入管线从文件中读取数据。
预加载数据： 在TensorFlow图中定义常量或变量来保存所有数据(仅适用于数据量比较小的情况)。

Reference:
http://tensorfly.cn/tfdoc/how_tos/reading_data.html
"""

with tf.Session() as sess:
    input = tf.placeholder(tf.float32)
    classifier = ...
    print classifier.eval(feed_dict={input: preprocess()})
    