import timeit
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

# vertex_cover_brute checks all possible sets of vertices of size k for a valid cover
def vertex_cover_brute(graph, res):
    vertices = list(dict(nx.to_dict_of_dicts(graph)).keys())
    k = len(vertices)
    # generate all edges present in graph
    edges = graph.edges
    for i in range(1, k):
        # generate all subset of size i from set vertices
        subsets_ = gen_subsets(vertices, i)
        for s in subsets_:
            # check if subset s is a cover for graph
            if verify_vertex_cover(s, edges) == True:
                # since subsets are generated in  increasing size, the first
                # subset that is cover can be returned as the minimal one
                res.append(s)
                return
    # no cover was found so return set of all edges as minimal cover
    #res.append(vertices)

# Generates all subsets of size k for the set given
# The subsets are generated in increasing size
def gen_subsets(set_, k):
    curr_subset = []
    res = []
    generate_subsets(set_, curr_subset, res, k, 0)
    return res

def generate_subsets(set_, curr_subset, subsets_, k, next_index):
    if len(curr_subset) == int(k):
        subsets_.append(curr_subset)
        return
    if next_index + 1 <= len(set_):
        curr_subset_exclude = curr_subset.copy()
        curr_subset.append(set_[next_index])
        generate_subsets(set_, curr_subset, subsets_, k, next_index+1)
        generate_subsets(set_, curr_subset_exclude, subsets_, k, next_index+1)

# verifies that cover is indeed a vertex cover
# does not check if cover only has vertices from graph
def verify_vertex_cover(cover, edges):
    # check that atleast one vertice from each edge appears in cover
    for edge in edges:
        in_cover = False;
        for vertex in cover:
            if edge[0] == vertex or edge[1] == vertex:
                    in_cover = True;
        # stop processing as soon as one edge found not in cover
        if in_cover == False:
            return False
    # return true if all edges have atleast one endpoint in cover
    return True
