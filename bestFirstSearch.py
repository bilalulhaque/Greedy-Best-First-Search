#Best First Search
import copy

romania = {
    'Arad':['Sibiu','Zerind','Timisoara'],
    'Sibiu':['Arad','Fagaras','Oradea','Rimnicu Vilcea'],
    'Zerind':{'Arad','Oradea'},
    'Timisoara':['Arad','Lugoj'],
    'Fagaras':['Sibiu','Bucharest'],
    'Oradea':['Zerind','Sibiu'],
    'Rimnicu Vilcea':['Sibiu','Pitesti','Craiova'],
    'Bucharest':['Fagaras','Pitesti','Urziceni','Giurgui'],
    'Pitesti':['Rimnicu Vilcea','Bucharest','Craiova'],
    'Craiova':['Rimnicu Vilcea','Pitesti','Dobreta'],
    'Urziceni':['Bucharest','Hirsova','Vasiui'],
    'Giurgui':['Bucharest'],
    'Hirsova':['Urziceni','Eforie'],
    'Vasiui':['Urziceni','Iasi'],
    'Eforie':['Hirsova'],
    'Iasi':['Vasiui','Neamt'],
    'Neamt':['Iasi'],
    'Lugoj':['Timisoara','Mehadia'],
    'Mehadia':['Lugoj','Dobreta'],
    'Dobreta':['Craiova','Mehadia']
}

h = {'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgui':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vasiui':199,
    'Zerind':374
}


def bestFirstSearch(start,final):
    path=[]
    priorityQueue=[[[start],h[start]]]
    visited=[]

    while priorityQueue!=[]:
        path.append(priorityQueue.pop(0))
        node=path[-1][0][-1]
        visited.append(node)

        if node == final:
            finalPath=copy.deepcopy(path[-1])
            print("Final path", finalPath)
            return "Found"

        for neighbor in romania[node]:
            if neighbor not in visited:
                newPath=copy.deepcopy(path[-1])
                newPath[0].append(neighbor)
                newPath[1]=h[neighbor]
                priorityQueue.append(newPath)
                # print(priorityQueue)

        priorityQueue.sort(key=lambda x:x[1])
        # print("Visited",visited)

bestFirstSearch('Arad','Bucharest')