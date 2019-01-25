#!/usr/bin/env python
# -*- coding:utf8 -*-

'''
kNN: k Nearest Neighbors
'''

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX, dataSet,labels, k):
    '''
    :param inX: 用于分类的输入向量
    :param dataSet:输入的训练样本集
    :param labels:标签向量
    :param k: number of neighbors to use for comparison (should be an odd number)
    :return:
    '''
    dataSetSize = dataSet.shape[0]
    print('dataSetSize:',dataSetSize)
    print('tile',tile(inX, (dataSetSize,1)))
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print('diffMat:',diffMat)
    sqDiffMat = diffMat**2
    print('sqDiffMat',sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    love_dictionary={'largeDoses':3, 'smallDoses':2, 'didntLike':1}
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if(listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector