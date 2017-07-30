from collections import defaultdict
from collections import deque
from heapq import *

def ImportGraph(graph):
    # Import a graph from a adjacency list
    v = open(graph,'r')  
    Graph = defaultdict(list)
  #  distance = []  
    for line in v.readlines():  
        VerDis = []
        d = deque(x for x in line.split())
        v1 = d.popleft()
        for z in d:
            for x in z.split(","):
                VerDis.append(x)
  #              distance.append(int(y))
        i = 0
        while i < len(VerDis):
            Graph[v1].append((int(VerDis[i+1]),VerDis[i]))
            i+=2

    v.close()  
    return Graph



def dijkstra(g, first, destination):
    q, visited = [(0,first,"The Shortest Path:")], []
    while 1:
        (cost,vertex,path) = heappop(q)
        if vertex not in visited:
            visited.append(vertex)
            path = path + "->" + vertex

            if vertex == destination: 
                return (cost, path)

            for cost2, vertex2 in g.get(vertex, ()):
                if vertex2 not in visited:
                    heappush(q, (cost+cost2, vertex2, path))

    #return float("inf")

if __name__ == "__main__":
    graph = ImportGraph("DijkstraData.txt")
    print(dijkstra(graph, "1", "7"))
    print(dijkstra(graph, "1", "37"))
    print(dijkstra(graph, "1", "59"))
    print(dijkstra(graph, "1", "82"))
    print(dijkstra(graph, "1", "99"))
    print(dijkstra(graph, "1", "115"))
    print(dijkstra(graph, "1", "133"))
    print(dijkstra(graph, "1", "165"))
    print(dijkstra(graph, "1", "188"))
    print(dijkstra(graph, "1", "197"))
