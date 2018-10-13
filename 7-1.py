# graph = {}
# graph['start']  ={}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# # print(graph['start'].keys())
# graph['a'] = {}
# graph['a']['fin'] = 1
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
# graph['fin'] = {}
# infiniy = float("inf")
# costs = {}
# costs['a'] = 6
# costs['b']  =2
# costs['fin']  = infiniy
# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None
# processed = []
#
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost<lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
# node = find_lowest_cost_node(costs)
# while node is not None:
#     cost = costs[node]
#     neighbor = graph[node]#找到邻居
#     for n in neighbor.keys():
#         new_cost = cost + neighbor[n]
#         if new_cost<costs[n]:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
#
# print(costs)







# costs['a'] = 5
# costs['b'] = 0
# costs['c'] = float("inf")
# costs['d'] = float("inf")
# costs['fin'] = float("inf")

# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['c'] = 'start'
# parents['d'] = 'start'
# parents['fin'] = None
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

# processed = []
def find_lowst(costs):
    low_cost = float("inf")
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node
# node = find_lowst(costs)
# while node is not  None:
#     cost = costs[node]
#     friends = graph[node]
#     for friend in friends.keys():
#         new_cost = friends[friend]+cost
#         # if new_cost <
#         if new_cost < costs[friend]:
#             costs[friend] = new_cost
#             parents[friend] = node
#     processed.append(node)
#     node = find_lowst(costs)
# print(costs['fin'])

#递归实现

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
