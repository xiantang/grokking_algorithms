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
# while states_needed:
#     bast_station = None
#     states_covered = set()
#     for station,state_for_station in stations.items():
#         # print(station,state_for_station)
#         covered  = state_for_station & states_needed
#
#         if len(covered) > len(states_covered):
#             bast_station = station
#             states_covered = covered
#     states_needed = states_needed - states_covered
#     # print(states_needed)
#
#     stations_array.append(bast_station) #最好的station
#
# print(stations_array)

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
