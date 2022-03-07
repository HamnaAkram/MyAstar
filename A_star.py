from queue import PriorityQueue as PQ

graph = {'Arad': [{'Zerind': [75]}, {'Timisoara': [118]}, {'Sibiu': [140]}],
         'Zerind': [{'Oradea': [71]}, {'Arad': [75]}],
         'Timisoara': [{'Lugoj': [111]}, {'Arad': [118]}],
         'Oradea': [{'Sibiu': [151]}, {'Zerind': [75]}],
         'Lugoj': [{'Mehadia': [70]}, {'Timisoara': [111]}],
         'Sibiu': [{'Fagaras': [99]}, {'Rimnicu Vilcea': [80]}, {'Arad': [140]}, {'Oradea': [151]}],
         'Mehadia': [{'Dobreta': [75]}, {'Lugoj': [70]}],
         'Dobreta': [{'Craiova': [120]}, {'Mehadia': [75]}],
         'Fagaras': [{'Bucharest': [211]}, {'Sibiu': [99]}],
         'Rimnicu Vilcea': [{'Pitesti': [97]}, {'Craiova': [146]}],
         'Craiova': [{'Rimnicu Vilcea': [146]}, {'Pitesti': [138]}],
         'Pitesti': [{'Bucharest': [101]}, {'Rimnicu Vilcea': [97]}],
         'Bucharest': [{'Urziceni': [85]}, {'Giurgiu': [90]}, {'Pitesti': [101]}, {'Fagaras': [211]}],
         'Giurgiu': [{'Bucharest': [90]}],
         'Urziceni': [{'Hirsova': [98]}, {'Bucharest': [85]}, {'Vaslui': [142]}],
         'Hirsova': [{'Urziceni': [98]}, {'Eforie': [86]}],
         'Eforie': [{'Hirsova': [86]}],
         'Vaslui': [{'Lasi': [92]}, {'Urziceni': [142]}],
         'Lasi': [{'Neamt': [87]}, {'Vaslui': [92]}],
         'Neamt': [{'Lasi': [87]}]
         }

cost = {'Arad': [366],
        'Bucharest': [0],
        'Craiova': [160],
        'Dobreta': [242],
        'Eforie': [161],
        'Fagaras': [178],
        'Giurgiu': [77],
        'Hirsova': [151],
        'Lasi': [226],
        'Lugoj': [244],
        'Mehadia': [241],
        'Neamt': [234],
        'Oradea': [380],
        'Pitesti': [98],
        'Rimnicu Vilcea': [193],
        'Sibiu': [253],
        'Timisoara': [329],
        'Urziceni': [80],
        'Vaslui': [199],
        'Zerind': [374]
        }


def AStar(graph, cost, snode, goal, path=[]):
    q = PQ();
    q.put((snode, 0))

    cameFrom = {snode: [0]}
    costSoFar = {snode: [0]}

    while q.empty() == False:
        currentNode = q.get()


        for node in graph[currentNode[0]]:
            for key in node.keys():
                newCost = int(costSoFar[currentNode[0]][0]) + int(node[key][0])
                if key not in costSoFar.keys() or newCost < int(costSoFar[key][0]):
                    costSoFar[key] = [newCost]
                    priority = newCost + int(cost[key][0])
                    q.put((key, priority))
                    cameFrom[key] = [currentNode[0]]
    return reconstructPath(cameFrom, snode, goal)


def reconstructPath(cameFrom, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current][0]
    path.append(start)
    path.reverse()
    return path


print("Current Path: ", AStar(graph, cost, 'Arad', 'Bucharest'))