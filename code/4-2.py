a = [1,2,3,4,5]
def sum(array):
    if array == []:
        return 0

    else:
        first = array[0]
        array.pop(0) #pop 指的是pop的索引
        return first + sum(array)

print(sum(a))