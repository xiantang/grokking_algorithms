a = [1, 2, 8, 4, 5]


def biggest(array):
    if array == []:
        return 0
    else:
        return array[0] if\
            array[0] > biggest(array[1:])\
            else biggest(array[1:])


print(biggest(a))
