a = [1,2,3,4,5]
def count(array):
    if array == []:
        return 0
    else:
        return 1+count(array[1:])
print(count(a))
