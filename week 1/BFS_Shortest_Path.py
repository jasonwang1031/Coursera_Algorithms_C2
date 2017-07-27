import queue
import collections
from collections import *


def BFS(graph, start):
    visited, queue = [start], collections.deque([start])
    distance = 1
    DisDict = []
    
    while queue:
        vertex = queue.popleft()
        for ConnectedVertex in graph[vertex]:
            if ConnectedVertex not in visited:
                visited.append(ConnectedVertex)
                queue.append(ConnectedVertex)
                d_ConnectedVertex = distance
                DisList.append(distance)
        distance +=1
        
    return max(DisList)

if __name__ == '__main__':
  #  graph = ImportGraph()
    graph = {0: [1, 2], 1: [0,2,3], 2: [0,1,3], 3:[1,2,4], 4:[3]} 
    c = BFS(graph,0)
    print(c)