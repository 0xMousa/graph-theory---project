from queue import PriorityQueue
from collections import defaultdict
q = PriorityQueue()
numberOfnode = 9
edge = {}
paths = PriorityQueue()
def addEdge(src , dest , w):
    if src not in edge.keys():
        edge[src] = [[w,dest]]
    else:
        edge[src].append([w , dest])
def addEdgeNonDirect(src , dest , w):
    addEdge(src , dest , w)
    addEdge(dest , src , w)
def addEdgeDirect(src , dest , w):
    addEdge(src, dest, w)
def getAllPaths(u , dest , visited , path , weight):
    visited[u] = True
    path.append(u)
    if u == dest:
        paths.put((weight , tuple(path)))
    else:
        for x in edge[u]:
            if not visited[x[1]]:
                getAllPaths(x[1], dest, visited, path , weight+x[0])
    path.pop()
    visited[u] = False


def dijkstra(src , d):
    dest = [1e9] * numberOfnode
    prev = [-1] * numberOfnode
    dest[src] = 0
    q = PriorityQueue()
    q.put( (0 , -1 , src) )
    while not q.empty():
        w , fro ,to = q.get()

        if (w > dest[to]): continue

        prev[to] = fro
        for x in edge[to]:
            #print(x)
            newW=x[0]
            newFROM= to
            newTO = x[1]
            if ( dest[newTO] > dest[newFROM] + newW):
                x[0] = dest[newTO] = dest[newFROM] + newW
                q.put((x[0] , newFROM, newTO))
    return dest


addEdgeNonDirect(0, 1, 4)
addEdgeNonDirect(0, 7, 8)
addEdgeNonDirect(1, 2, 8)
addEdgeNonDirect(1, 7, 11)
addEdgeNonDirect(2, 3, 7)
addEdgeNonDirect(2, 8, 2)
addEdgeNonDirect(2, 5, 4)
addEdgeNonDirect(3, 4, 9)
addEdgeNonDirect(3, 5, 14)
addEdgeNonDirect(4, 5, 10)
addEdgeNonDirect(5, 6, 2)
addEdgeNonDirect(6, 7, 1)
addEdgeNonDirect(6, 8, 6)
addEdgeNonDirect(7, 8, 7)

visited = [False] * (numberOfnode+2)
path = []
weight = 0
getAllPaths(0, 4, visited, path, weight)
while not paths.empty():
    print(paths.get())