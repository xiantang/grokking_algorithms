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