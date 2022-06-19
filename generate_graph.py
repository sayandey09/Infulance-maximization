from igraph import *

def generate(valGraph,valNode):
    node = 100
    graphList = []
    for _ in range(valGraph):
        graph = Graph.Barabasi(n=node, m=3,directed=True)
        node = node + valNode
        graphList.append(graph)
    
    return (graphList)