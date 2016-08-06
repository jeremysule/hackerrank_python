# def dfs_cycle(graph, start, seen):
#     seen[start] = start
#     to_visit=[start]
#     while to_visit:
#         node = to_visit.pop()
#         for neihbor in graph.setdefault(node,[]):
#             if neihbor == start:
#                 return True
#             seen[neihbor] = True
#             to_visit.append(neihbor)
#     return False
#
# def isThereACycle(friendList):
#     # for n in set(friendList.keys()):
#     #     if dfs_cycle(friendList, n, {}):
#     #         return "ORDER VIOLATION"
#     n = set(friendList.keys()).pop()
#     if dfs_cycle(friendList, n, {}):
#         return "ORDER VIOLATION"
#     return "ORDER EXISTS"
#
# x = int(input()) #nb of trips
#
# for _ in range(x):
#
#     n = int(input()) #nb of attractions
#     friendList = []
#     for __ in range(n):
#         friend = input().split(',')
#         friendList.append(friend)
#
#
#     graph_adj_list = {} # att -> [neighbours]
#     for f in friendList:
#         for i in range(len(f) -1):
#             list = graph_adj_list.setdefault(f[i], [])
#             list.append(f[i+1])
#
#     res = isThereACycle(graph_adj_list)
#     print(res)





x = int(input()) #nb of trips

for _ in range(x):

    n = int(input()) #nb of attractions
    friendList = []
    for __ in range(n):
        friend = input().split(',')
        friendList.append(friend)

    allAttractions = set()
    graph_adj_list = {} # att -> [neighbours]
    for f in friendList:
        for i in range(len(f) -1):
            allAttractions.add(f[i])
            allAttractions.add(f[i+1])
            list = graph_adj_list.setdefault(f[i], [])
            list.append(f[i+1])
    matrix = []
    dim = len(allAttractions)
    for (i,j) in [(i,j) for i in range(dim) for j in range(dim)]:




    # res = isThereACycle(graph_adj_list)
    # print(res)
