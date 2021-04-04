# 图解算法代码
  这是本人在18年学习《图解算法》时候学习留下的代码和相应的思考，这本书是一本很不错的算法书籍，如果认真阅读思考可以为你的算法打下不错的基础，在阅读了这本书之后可以去阅读《算法4th》《算法导论》等书，同时也可以辅以 leetcode 练习实践一下。    
  对于这个仓库的问题和疑问欢迎在 issue 区讨论或者提出 MR 修改代码👏。

### 二分查找
```python
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
```
这个思路主要是不断中断数组
然后判断是否在中点上  
* 疑问: 为什么判断错误之后 mid 要+1/-1呢?
* 回答: 画了张图理解了一下 主要是把猜错的中点给排除掉


### 选择排序

```python
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
```
* 疑问:为什么循环`len(array)`次就可以完成了排序?
* 回答:因为数组长度是`len(array)`,每次都会弹出一个元素,
弹`len(array)`次就会让原数组为空.

### 数组链表区别 

* 数组元素是在一起的/列表是分开的,每个元素到都存储了下一个元素的地址  
* 数组读取,随机读取很快/链表插入删除很快.
* 数组中所有元素都是一个类型.

### 递归 
```python
def countdown1(i):
    print(i)
    countdown1(i-1)
# countdown(1)

def countdown2(i):
    print(i)
    if i<=1:#基线条件
        return
    else: #递归条件
        countdown2(i-1)

a=countdown2(3)
```
递归主要由两个部分组成:   
    1. 递归条件:函数调用自己   
    2. 基线条件:函数不再调用自己  
### 调用栈
* 当调用另一个函数时候,当前函数处于未完成状态.
```python
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)#塞入栈中 #fact函数没有结束
```

### 递归总结
* 递归指的是调用自己的函数
*   1. 递归条件:函数调用自己   
    2. 基线条件:函数不再调用自己
* 两种操作1.压入栈中 2.弹出栈
* 所有函数都进入调用栈  
* 调用栈很长就会很占用内存

### D&C算法 
```python
def DC(x,y):
    if x>y:
        x=x%y
        if x ==0:#基线条件
            return y
        return DC(x,y)
    if x<y:
        y=y%x
        if y ==0:
            return x
        return DC(x,y)
```
分治法思路
1. 找出基线条件/尽可能简单 
2. 不断分割问题->符合基线条件
#### 求和
```python
#我写的
a = [1,2,3,4,5]
def sum(array):
    if len(array) ==0 :
        return 0
    if len(array) ==1 :
        return array[0]
    else:
        first = array[0]
        array.pop(0) #pop 指的是pop的索引
        return first + sum(array)

print(sum(a))
```

```python
#标准答案
a = [1,2,3,4,5]
def sum(array):
    if array == []:
        return 0
    else:
        return array[0] + sum(array[1:])

print(sum(a))
```

数组求和问题
1. 将数组问题分割成数组第一个元素之后的元素和第一个元素相加  
2. 涉及数组的递归函数时候,基线条件通常是数组为空/只包含一个元素

#### 求数目

```python
a = [1,2,3,4,5]
def count(array):
    if array == []:
        return 0
    else:
        return 1+count(array[1:])
print(count(a))
```

### 求最大值 

```python
a = [1, 2, 8, 4, 5]


def biggest(array):
    if array == []:
        return 0
    else:
        return array[0] if\
            array[0] > biggest(array[1:])\
            else biggest(array[1:])
print(biggest(a))
```

* 或许我们接触的是for循环/如果我们用递归呢?
使用递归实现二分法
```python
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
```
* 基线条件
    1. 只剩下一个元素,就是那个需要的元素
    2. 中点直接是猜到的元素
* 递归条件
    1. 猜的元素比中点大
    2. 猜的元素比中点小
    
    
### qsort

```python
a = [1,2,6,3,8,5]

def qsort(array):
    if len(array) < 2:
        return array
    mid = array[0]
    low = [array[i] for i in range(1,len(array)) if array[i] <= mid]
    up = [array[i] for i in range(1,len(array)) if array[i] > mid]
    return qsort(low)+[mid]+qsort(up)
print(qsort(a))
```
1. 选择基准值
2. 分别找出比基准大的值和比基准小的值
3. 递归的对子数组进行排序

##### 归纳证明
1. 基线条件
2. 归纳条件 证明排序len=1的数组有用 len=2 有用 len=3有用
所以之后无需证明都有效 

###大O表示法
结论:
* 指明的是算法的增速
* 指出的是算法的最糟运行时间
* 不考虑`+*-/`
* 通常不考虑常量(快速查找常量比归并小)

### qsort 时间复杂度
* 最糟糕(头)
    1. 以头为基准,需要涉及整个列表
    2. 因为要遍历两边的数组,而且O(n)不受常量影响
* 最优(中间)
    1. 以中间为基准(类似二分log n)
    2. 每层O(n)
最佳的就是平均的情况 
TODO: 随机的选择用作基准的元素

```python
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
```

### 散列表 

DNS 解析
域名->ip地址


### 广度优先遍历

```python
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
find()
```
使用一个队列 从右侧加入一个节点的所有的下个节点
然后从左侧读取一个节点 往返直到队列为空 

```python
from collections import deque
def person_is_seller(name):
    return name[-1] == 'm'
graph = {}
graph['you'] = ["alice","bob","claire"]
graph['bob'] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jooy"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue = deque()

def find2(search_queue):
    if search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person +"is seller")
            return True
        else:
            search_queue +=graph[person]
        return find2(search_queue)
    else:
        return None

search_queue += graph["you"]
print(find2(search_queue))
```

* 广度优先遍历是找到是否A-B的
* 有就可以找到最短路径
* 有向图可以指定方向
* 无向图关系双向
* 按照顺序放入队列就可以找到最短路径,检查过的人需要放入去重列表

### 迪杰斯特拉算法

```python
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 0
graph['a'] = {}
graph['a']['c'] = 15
graph['a']['d'] = 20
graph['b'] = {}
graph['b']['c'] = 30
graph['b']['d'] = 25
graph['c'] = {}
graph['c']['fin'] = 20
graph['d'] = {}
graph['d']['fin'] = 10
graph['fin'] = {}
costs = {}



costs['a'] = 5
costs['b'] = 0
costs['c'] = float("inf")
costs['d'] = float("inf")
costs['fin'] = float("inf")
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = 'start'
parents['d'] = 'start'
parents['fin'] = None
processed = []
def find_lowst(costs):
    low_cost = float("inf")
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node

node = find_lowst(costs)
while node is not  None:
    cost = costs[node]
    friends = graph[node]
    for friend in friends.keys():
        new_cost = friends[friend]+cost
        # if new_cost <
        if new_cost < costs[friend]:
            costs[friend] = new_cost
            parents[friend] = node
    processed.append(node)
    node = find_lowst(costs)
print(costs)
```

简洁版本

```python
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 0
graph['a'] = {}
graph['a']['c'] = 15
graph['a']['d'] = 20
graph['b'] = {}
graph['b']['c'] = 30
graph['b']['d'] = 25
graph['c'] = {}
graph['c']['fin'] = 20
graph['d'] = {}
graph['d']['fin'] = 10
graph['fin'] = {}
def get_costs_parent(graph):
    costs = {}
    parents = {}
    for node in graph.keys():
        if node in graph['start'].keys():
            costs[node] = graph['start'][node]
            parents[node] = 'start'
        else:
            costs[node] = float('inf')
            parents[node] = None
    return costs,parents
costs ,parents= get_costs_parent(graph)

processed = []
def find_lowst(costs):
    low_cost = float("inf")
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node
node = find_lowst(costs)
while node is not  None:
    cost = costs[node]
    friends = graph[node]
    for friend in friends.keys():
        new_cost = friends[friend]+cost
        # if new_cost <
        if new_cost < costs[friend]:
            costs[friend] = new_cost
            parents[friend] = node
    processed.append(node)
    node = find_lowst(costs)
print(costs['fin'])
```

```python
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 0
graph['a'] = {}
graph['a']['c'] = 15
graph['a']['d'] = 20
graph['b'] = {}
graph['b']['c'] = 30
graph['b']['d'] = 25
graph['c'] = {}
graph['c']['fin'] = 20
graph['d'] = {}
graph['d']['fin'] = 10
graph['fin'] = {}
def get_costs_parent(graph):
    costs = {}
    parents = {}
    for node in graph.keys():
        if node in graph['start'].keys():
            costs[node] = graph['start'][node]
            parents[node] = 'start'
        else:
            costs[node] = float('inf')
            parents[node] = None
    return costs,parents
costs ,parents= get_costs_parent(graph)

def find_lowst(costs):
    low_cost = float("inf")
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node
def find_short_path(costs,processed,parents):
    node = find_lowst(costs)
    if node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = neighbors[n] + cost
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        return find_short_path(costs,processed,parents)

    else:
        return costs['fin']
processed = []

fastst = find_short_path(costs,processed,parents)
```

递归实现:
* 基准条件:找到的最小节点为空
* 递归条件:还有节点没有处理

#### 主要思路:
1. 找到一个节点然后取找他的所有相邻节点
2. 将相邻节点到本节点的距离与本节点到起点的距离相加
3. 判断是否比相邻结点原来的距离短
4. 如果更短直接更新,并且加入去重列表
5. 如何取找一个节点:我们选取的是最小的节点,如果这个节点不在去重队列
并且是最小的,就以他为节点更新他的相邻节点,至于我们要选择最小的,是因为
要是选择最大的化会遇到无限大的情况(没有找到到达线路)

* 广度优先搜索可用来在非加权图中查找最短路径
* Dijkstra适合在加权图中查找最短路径
* 加权图为正:Dijkstra/加权图为负:贝尔曼-福德

### 贪心算法

```python
array = ['mt','wa','or','id','nv','ut','ca','az']
states_needed = set(array)
# 转换为集合
stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])
stations_array = []
while states_needed:
    bast_station = None
    states_covered = set()
    for station,state_for_station in stations.items():
        # print(station,state_for_station)
        covered  = state_for_station & states_needed

        if len(covered) > len(states_covered):
            bast_station = station
            states_covered = covered
    states_needed = states_needed - states_covered
    # print(states_needed)

    stations_array.append(bast_station) #最好的station

print(stations_array)
```

* 贪心算法思路:每步都选择最有解,从而达到整体最优解
* 不适用场景:背包问题/只能找到非常接近最优解的解法

```python

#递归实现
def find_station(states_needed):
    if states_needed:
        bast_station = None
        states_covered = set()
        for station,state_for_station in stations.items():
            # print(station,state_for_station)
            covered  = state_for_station & states_needed

            if len(covered) > len(states_covered):
                bast_station = station
                states_covered = covered
        states_needed = states_needed - states_covered

        return  [bast_station] +find_station(states_needed)
    else:
        return []
print(find_station(states_needed))

```
实现思路:
1.寻找覆盖未被覆盖区域最多的电台  
2.将这个加入队列
3.更新未被覆盖区域
4.重复1-3

### NP完全问题
1. 元素较少运行速度快,元素越来越多速度会变得非常慢.
2. 涉及所有组合的通常是NP完全问题
3. 不能分割成小问题,需要考虑各种情况的
4. 问题涉及旅行商序列等的且难以解决的
5. 问题涉及广播台集合的
6. 问题可以转换为旅行商或者集合覆盖的问题的

```python
graph = {}
graph['a'] = {}
graph['a']['b'] = 3
graph['a']['c'] = 6
graph['a']['d'] = 1
graph['c'] = {}
graph['c']['a'] = 6
graph['c']['b'] = 2
graph['c']['d'] = 7
graph['b'] = {}
graph['b']['c'] = 2
graph['b']['d'] = 5
graph['b']['a'] = 3
graph['d'] = {}
graph['d']['c'] = 7
graph['d']['a'] = 1
graph['d']['b'] = 5

list_city_array=list(graph.keys())

def find_fast(graph,next_array):
    if next_array:
        finded_array = []
        city = next_array.pop()
        list_array = list(graph.keys())
        cost = 0

        finded_array.append(city)
        while len(finded_array) < len(list_array):

            low_cost = float('inf')
            low_cost_city = None
            for neibo in graph[city].keys():
                if graph[city][neibo]<low_cost and neibo not in finded_array:
                    low_cost = graph[city][neibo]
                    low_cost_city = neibo

            # print(low_cost)
            cost += low_cost
            finded_array.append(low_cost_city)

            city = low_cost_city

        mined =  min(find_fast(graph,next_array),cost)
        return mined
    else:

        return float("inf")


print(find_fast(graph,list_city_array))
```
旅行商问题使用近似算法实现
* 基准条件:剩余被查找队列为空
* 递归条件:剩余查找队列不为空
1.从城市列表中获得一个城市  
2.寻找这个城市最近距离的城市,且不再已查找列表
3.更新时间花费,将被查找城市加入已查找队列  
4.以这个城市为起点查找最近距离城市
5.重复2-4

### 动态规划
问题:为什么第一排每个单元格都是1500?
回答:第一个单元格指的是第一个1磅时候最大价格是1500
第二个单元格指的是2磅的时候价格是1500 以此类推

我想应该把他们分开
