import math
def bina_search(list,item):
    low = 0
    hight = len(list)-1
    while low<=hight:
        #每次猜测
        mid = math.floor((low + hight)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid-1
        else:
            low = mid+1
    return None

my_list = [1,3,5,7,8]

print(bina_search(my_list,7))