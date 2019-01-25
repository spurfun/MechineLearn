import trees

def test1():
    dataSet, labels = trees.createDataSet()
    print(dataSet)
    print(labels)
    # print(trees.calcShannonEnt(dataSet))
    # print(trees.splitDataSet(dataSet,0,0))
    print(trees.chooseBestFeatureToSplit(dataSet))

if __name__ == '__main__':
    test1()