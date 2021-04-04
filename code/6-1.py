from collections import deque

graph = {}
graph['you'] = ["alice","bob","claire"]
graph['bob'] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jooy"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'
# deque

def find():
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person +"is seller")
            return True
        else:
            search_queue +=graph[person]
    return False
# find()
search_queue = deque()
array = []
def find2(search_queue,array):
    if search_queue:
        person = search_queue.popleft()
        if person in array:
            print(person+" is in array")
            return find2(search_queue,array)
        if person_is_seller(person):
            print(person +"is seller")
            return True
        else:

            array.append(person)
            search_queue +=graph[person]
        return find2(search_queue,array)
    else:
        return None


search_queue += graph["you"]
print(find2(search_queue,array))
array = [1,3,56,3,62,5]
#
# def qsort(array):
#     if len(array)<2:
#         return array
#     else:
#         mid = array[0]
#         smaller = [i for i in array[1:] if i<mid]
#         bigger = [i for i in array[1:] if i>=mid]
#         return qsort(smaller) +[mid] +qsort(bigger)
#
# print(qsort(array))