array = [5,7,2,4,3,1,8,6]
from random import randint
def qsort(array):

    if len(array)<=1:
        return array
    ran=randint(0,len(array)-1)

    mid = array[ran]
    array.pop(ran)
    smaller = [ i for i in array   if i<=mid]
    bigger = [i for i in array  if i>mid ]
    return  qsort(smaller) + [mid] +qsort(bigger)

print(qsort(array))
