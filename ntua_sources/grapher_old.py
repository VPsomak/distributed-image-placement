#	This file is part of Distributed Image Placer.
#
#    Distributed Image Placer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Distributed Image Placer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Distributed Image Placer.  If not, see https://www.gnu.org/licenses/.

import string, random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.random
from math import floor

random.seed(10)
numpy.random.seed(10)
imageSize = 3*1024*1024*1024
bandwidthEthernet = 10*1024*1024*1024
bandwidthWifi = 25*1024*1024

def draw_continuum(filename: string, color_map, graph, mode=None):
    
    edge_labels = nx.get_edge_attributes(graph, 'percentage')
    
    drawFuncs = [nx.draw,nx.draw_circular,nx.draw_kamada_kawai,nx.draw_planar,nx.draw_random,nx.draw_spectral,nx.draw_spring,nx.draw_shell]
    drawLayouts = [nx.drawing.layout.spiral_layout,nx.drawing.layout.circular_layout,nx.drawing.layout.kamada_kawai_layout,nx.drawing.layout.planar_layout,nx.drawing.layout.random_layout,nx.drawing.layout.spectral_layout,nx.drawing.layout.spring_layout,nx.drawing.layout.shell_layout]
    if mode is None:
        nx.draw(graph, node_size=120, node_color=color_map, linewidths=0.1, font_size=6, font_weight='bold', with_labels=True)
    else:
        pos = drawLayouts[mode](graph)
        drawFuncs[mode](graph, node_size=120, node_color=color_map, linewidths=0.1, font_size=6, font_weight='bold', with_labels=True)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)
        
    plt.savefig(filename, dpi=400)
    plt.show()
    plt.clf()

def create_continuum(size=20, degree = 2):
    # Graph creation
    # G = nx.star_graph(NUM_EDGES)
    G2 = nx.barabasi_albert_graph(size, degree)
    # G2 = nx.generators.classic.balanced_tree(8, 2)
    # G2 = nx.generators.classic.binomial_tree(size)

    NODES = G2.number_of_nodes()
    NUM_NODES_ACTIVATED = floor(NODES / 1)
    NUM_NODES_WITH_IMAGE = floor(NODES / 3)

    # Attributes to the graph
    edgeCapacities = {}
    for node in G2.edges:
        if random.random() < 0.7:
            edgeCapacities[node] = bandwidthWifi
        else:
            edgeCapacities[node] = bandwidthEthernet
    nx.set_edge_attributes(G2, values=edgeCapacities, name='capacity')
    nx.set_edge_attributes(G2, values=0, name='usage')
    nx.set_edge_attributes(G2, values=0, name='percentage')

    # Nodes to activate
    nodes_activated = np.random.choice(NODES, NUM_NODES_ACTIVATED, replace=False)
    print(f"nodes activated {nodes_activated}")

    # Nodes with image
    nodes_with_image = np.random.choice(NODES, NUM_NODES_WITH_IMAGE, replace=False)
    print(f"nodes nodes_with_image {nodes_with_image}")

    betweenness_cent = nx.betweenness_centrality(G2)
    print(betweenness_cent)

    degree_cent = nx.degree_centrality(G2)
    print(degree_cent)

    # nx.set_node_attributes(G2, bc, "betweenness")
    sorted_betweenness_cent = sorted(betweenness_cent, key=lambda x: betweenness_cent[x], reverse=True)
    print(sorted_betweenness_cent)

    sorted_degree_cent = sorted(degree_cent, key=lambda x: degree_cent[x], reverse=True)
    print(sorted_degree_cent)

    # Top k nodes
    nodes_with_image = sorted_betweenness_cent[:NUM_NODES_WITH_IMAGE]

    # Compute shortest paths
    shortest_paths = nx.shortest_path(G2)

    # find the image at a least amount of hops
    nearest_image = []
    for active_node in nodes_activated:
        nearest_image.append(min(nodes_with_image, key=lambda x: len(shortest_paths[active_node][x])))
        
    for i in range(len(nodes_activated)):
        sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
        print (f"Shortest Path from {nodes_activated[i]} to {nearest_image[i]} is {sp}")
        for j in range(len(sp) - 1):
            G2[sp[j]][sp[j + 1]]['usage'] +=imageSize
            G2[sp[j]][sp[j + 1]]['percentage'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
            print(f"Usage of channel {sp[j]} to {sp[j+1]} is {G2[sp[j]][sp[j + 1]]['percentage']*100}")

    sp_capacity = []
    for i in range(len(nodes_activated)):
        sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
        if nodes_activated[i] == nearest_image[i]:
            sp_capacity.append((nodes_activated[i], float('inf')))
        else:
            sp_capacity.append((nodes_activated[i], min([G2[sp[i]][sp[i+1]]['capacity']/G2[sp[i]][sp[i+1]]['usage'] for i in range(len(sp)-1) if not nodes_activated[i] == nearest_image[i]])))

    print(f"Max Capacities {sp_capacity}")

    color_map = []
    for node in G2:
        if node in nodes_activated:
            if node in nodes_with_image:
                color_map.append('green')
            else:
                color_map.append('cyan')
        elif node in nodes_with_image:
            color_map.append('red')
        else:
            color_map.append('orange')

    # for mode in range(0,8):
        # draw_continuum("mode_"+str(mode)+".png", color_map, G2, mode)
    draw_continuum("mode_"+str(2)+".png", color_map, G2, 2)
    
create_continuum()