from numpy import *
import operator

#给出训练数据
def createDataSet():
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels = ['A','A','B','B']
    return group,labels
#通过KNN分类
def classify(input,dataSet,label,k):
    #获取维度 x
    dataSize = dataSet.shape[0]
    #和训练集维度相同的
    dataSet_new=tile(input,(dataSize,1))
    diff = dataSet_new-dataSet
    sqdiff = diff**2 #求差值平方
    # print(sqdiff)
    squareDist = sum(sqdiff,axis=1)#行向量相加
    dis = squareDist ** 0.5#开平方
    print(
        dis
    )
    sortedDistIndex = argsort(dis) #排序提取其索引
    print(sortedDistIndex)
    classCount = {}
    for i in range(k): #选取k个邻居
        #sortedDistIndex[i]的值为距离

        voteLabel = label[sortedDistIndex[i]] #??最近邻居吗 这明显有问题
        #get()第二个值是默认值为0
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
        #给字典的value 自加

    maxCount = 0
    classes = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes
    # print(classCount)
if __name__ == '__main__':
    group,labels = createDataSet()
    k=3
    input = array([1.1,0.1])
    print(classify(input,group,labels,k))
