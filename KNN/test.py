#!/usr/bin/env python
# -*- coding:utf8 -*-
import kNN
import matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    datingDataMat,datingLables = kNN.file2matrix('datingTestSet.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    plt.show()