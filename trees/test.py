import trees

def test1():
    dataSet, labels = trees.createDataSet()
    print(dataSet)
    print(labels)
    print(trees.calcShannonEnt(dataSet))
    # for featVec in dataSet:
    #     print(featVec[-1])
if __name__ == '__main__':
    test1()