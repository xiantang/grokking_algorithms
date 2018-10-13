def find_small(arry:list)->int:
    """
    找到最小的元素
    :param arry:
    :return:
    """
    smallest = arry[0]
    smallest_index = 0
    for i in range(1,len(arry)):
        if smallest>arry[i]:
            smallest = arry[i]
            smallest_index = i
    return smallest_index


def selectionSort(arry:list)->list:
    """
    选择排序
    :param arry:
    :return:
    """

    new_array = []
    for i in range(len(arry)):
        smallest = find_small(arry)
        new_array.append(arry.pop(smallest))
    return new_array

print(selectionSort([5,3,6,2,10]))