
import math
a = [1, 2, 3, 4, 5, 8, 10]
def cut(array, item):
    len_array = len(array)
    if len_array == 1:
        return 0
    else:
        mid = math.floor(len_array / 2)
        if item == array[mid]:
            return mid
        if item > array[mid]:
            return len(array[:mid]) + cut(array[mid:], item)
        else:
            return cut(array[:mid], item)
print(cut(a, 8))
