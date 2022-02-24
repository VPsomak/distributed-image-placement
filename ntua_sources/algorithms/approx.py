import timeit
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


def vertex_cover_approx(graph, size_, res):
    # generate all edges present in graph
    edges = graph.edges
    s = 0
    cover_ = []
    for edge in edges:
        if edge[0] not in cover_ and edge[1] not in cover_:
            cover_.append(edge[0])
            cover_.append(edge[1])
            s += 2
    size_.append(s)
    res.append(cover_)
