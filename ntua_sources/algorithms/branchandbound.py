import networkx as nx
import operator
import time
import os
import math
import argparse
import matplotlib.pyplot as plt

T=600

# returns the max degree node in a given any graph
def max_deg(g):
    d_list = g.degree()
    degree_sorted = sorted(g.degree, key=lambda x: x[1], reverse=True)
    return degree_sorted[0]

def Branch_and_Bound(G, res):
    start_time = time.time()
    end_time = start_time
    time_diff = end_time - start_time
    Current_Graph = G.copy()  # Current_Graph: sub-graph of current graph after removing the explored nodes
    Best_Vertex_Cover = []  # Best_Vertex_Cover: min (best) Vertex cover for a given sub-graph
    Current_VC = []  # Current_VC: Vertex cover for a given sub-graph
    Frontier = []
    vertex = max_deg(Current_Graph)
    Frontier.append((vertex[0], 0, (5, 5)))
    Frontier.append((vertex[0], 1, (5, 5)))
    neighbor = []
    UP_Bound = G.number_of_nodes()
    times_list = []

    while (Frontier) != [] and time_diff < T:
        (vertex_i, state, parent_node) = Frontier.pop()  # the current node, last node of the Frontier set
        if state == 1:  # assign state =1
            Current_Graph.remove_node(vertex_i)  # remove the vertex from Current_Graph
            Current_VC.append((vertex_i, state))  # append the vertex to the Vertex Cover
        elif state == 0:  # assign state =0
            neighbor = Current_Graph.neighbors(vertex_i)
            for node in list(neighbor):
                Current_Graph.remove_node(node)  # remove the neighbor of the vertex from Current_Graph
                Current_VC.append((node, 1))  # add all the neigbor to the Vertex Cover
        if (Current_Graph.number_of_edges() == 0):  # done exploring
            if len(Current_VC) < UP_Bound:
                Best_Vertex_Cover = Current_VC.copy()
                UP_Bound = len(Current_VC)
                times_list.append((len(Current_VC), time.time() - start_time))
            if (len(Frontier) != 0):  # backtrack to explore other nodes
                last_frontier = Frontier[-1][2]  # parent node
                if last_frontier in Current_VC:
                    while (Current_VC.index(last_frontier) + 1 < len(
                            Current_VC)):  # undoing changes from the end of current Vertex cover to parent node
                        node_i, state_i = Current_VC.pop()  # remove what we added to Current Vertex Cover
                        list_of_nodes = list(map(lambda t: t[0], Current_VC))
                        Current_Graph.add_node(node_i)  # add back what we deleted from the Current Graph
                        for node in G.neighbors(node_i):
                            if (node in Current_Graph.nodes()) and (node not in list_of_nodes):
                                Current_Graph.add_edge(node, node_i)
                else:  # back track to the root node
                    Current_Graph = G.copy()
                    Current_VC.clear()
        else:
            lb = Current_Graph.number_of_edges() / max_deg(Current_Graph)[1]  # lower bound calcuation
            Current_LowerBound = int(lb) + len(Current_VC)  # reset lower bound
            if (UP_Bound > Current_LowerBound):  # worth exploring
                vertex_j = max_deg(Current_Graph)
                Frontier.append((vertex_j[0], 0, (vertex_i, state)))  # assign state =0 and add to Frontier set
                Frontier.append((vertex_j[0], 1, (vertex_i, state)))  # assign state =1 and add to Frontier set
            else:  # backtrack to explore other nodes.
                if (len(Frontier) != 0):
                    last_frontier = Frontier[-1][2]  # parent node
                    if last_frontier in Current_VC:
                        while (Current_VC.index(last_frontier) + 1 < len(
                                Current_VC)):  # undoing changes from the end of current Vertex cover to parent node
                            node_i, state_i = Current_VC.pop()  # remove what we added to Current Vertex Cover
                            list_of_nodes = list(map(lambda t: t[0], Current_VC))
                            Current_Graph.add_node(node_i)  # add back what we deleted from the Current Graph
                            for node in G.neighbors(node_i):
                                if (node in Current_Graph.nodes()) and (node not in list_of_nodes):
                                    Current_Graph.add_edge(node, node_i)
                    else:  # back track to the root node
                        Current_Graph = G.copy()
                        Current_VC.clear()
        end_time = time.time()
        time_diff = end_time - start_time
        if time_diff > T:
            print('time expired')
    # print ("Bes", Best_Vertex_Cover)
    temp_typle = [(t[0]) for t in Best_Vertex_Cover]
    lst = [temp_typle for i in range(1)]
    res.append(lst)
    return (Best_Vertex_Cover, res)