import queue
import collections
from collections import *

def ImportGraph(graph):
    # Import a graph through a text file of adjacency list
    v = open(graph,'r')  
    GraphDict = {}  
    for line in v.readlines():  
        vertex=[int(x) for x in line.split()]  
        GraphDict[vertex[0]]=set(vertex[1:])  
    v.close()  

    return GraphDict, EdgeList

def BFS(graph, start):
    visited, queue = [start], collections.deque([start])
    while queue:
        vertex = queue.popleft()
        for ConnectedVertex in graph[vertex]:
            if ConnectedVertex not in visited:
                visited.append(ConnectedVertex)
                queue.append(ConnectedVertex)
    return visited

if __name__ == '__main__':
  #  graph = ImportGraph()
    graph = {0: [1, 2], 1: [0,2,3], 2: [0,1,3], 3:[1,2,4], 4:[3]} 
    c = BFS(graph,0)
    print(c)
