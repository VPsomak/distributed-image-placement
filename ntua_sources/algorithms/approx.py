import timeit
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

# Approximation: https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf

# vertex_cover_approx
# Generates an approximately optimal vertex cover for a given graph using the APPROX-VERTEX-COVER algorithm
# found in (Cormen)
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
