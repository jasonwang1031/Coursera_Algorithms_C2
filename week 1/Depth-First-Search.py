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

def DFS(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)

    for ConnectedVertex in graph[start]:
        if ConnectedVertex not in visited:
            DFS(graph,ConnectedVertex,visited)

    return visited

if __name__ == '__main__':
  #  graph = ImportGraph()
    graph = {0: [1, 2], 1: [0,2,3], 2: [0,1,3], 3:[1,2,4], 4:[3]} 
    c = DFS(graph,0)
    print(c)
