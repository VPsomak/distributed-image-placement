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

import string, random, sys
from algorithms import ilp, approx, bruteForce, greedy, branchandbound, genetic
import maxmin
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.random
import time
from networkx.algorithms import approximation
from math import floor
# import satispy

random.seed(10)
numpy.random.seed(10)
imageSize = 3*1024*1024*1024

# 10737418240
bandwidthEthernet = 10*1024*1024*1024
# 26214400
bandwidthWifi = 25*1024*1024
# 524288
bandwidthlocalfile = 0.5*1024*1024


if len(sys.argv) == 3:
    model = sys.argv[1]
    graph = sys.argv[2]
else:
    print ("Wrong number of arguments!\n")
    print ("Example: python3 grapher.py [model] [algorithm] \n")
    print ("Available models [ilp, approximation, bruteforce, branchandbound, genetic] \n")
    print ("Available graphs [binomial_tree, balanced_tree, star, barabasi_albert, erdos_renyi, newman_watts_strogatz]")
    sys.exit()


def draw_continuum(filename: string, color_map, graph, mode=None):
    
    edge_labels = nx.get_edge_attributes(graph, 'time')
    
    drawFuncs = [nx.draw,nx.draw_circular,nx.draw_kamada_kawai,nx.draw_planar,nx.draw_random,nx.draw_spectral,nx.draw_spring,nx.draw_shell]
    drawLayouts = [nx.drawing.layout.spiral_layout,nx.drawing.layout.circular_layout,nx.drawing.layout.kamada_kawai_layout,nx.drawing.layout.planar_layout,nx.drawing.layout.random_layout,nx.drawing.layout.spectral_layout,nx.drawing.layout.spring_layout,nx.drawing.layout.shell_layout]
    if mode is None:
        nx.draw(graph, node_size=120, node_color=color_map, linewidths=0.1, font_size=6, font_weight='bold', with_labels=True)
    else:
        pos = drawLayouts[mode](graph)
        drawFuncs[mode](graph, node_size=120, node_color=color_map, linewidths=0.1, font_size=6, font_weight='bold', with_labels=True)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)
        
    #plt.savefig(filename, dpi=400)
    plt.show()
    plt.clf()
    
def getScore(graph,placement):
    score = len(placement) + sum([graph.edges[edge[0],edge[1]]['usage']/graph.edges[edge[0],edge[1]]['capacity'] for edge in graph.edges])
    return score

def create_continuum(size=10, degree=2, branching_factor_of_tree=4, height_of_tree=2, knearest=7, probability=0.7):
    # Graph creation

    if graph =="binomial_tree":
        G2 = nx.generators.classic.binomial_tree(size)
    elif graph =="balanced_tree":
        G2 = nx.generators.classic.balanced_tree(branching_factor_of_tree, height_of_tree)
    elif graph =="star":
        G2 = nx.star_graph(size)
    elif graph =="barabasi_albert":
        G2 = nx.barabasi_albert_graph(size, degree)
    elif graph =="erdos_renyi":
        G2 = nx.erdos_renyi_graph(size, probability, seed=None, directed=False)
    elif graph =="newman_watts_strogatz":
        G2 = nx.newman_watts_strogatz_graph(size, knearest, probability, seed=None)
    else:
        print ("Give a correct graph as indicated from the list\n")
        print("Available graphs [binomial_tree, balanced_tree, star, barabasi_albert, erdos_renyi, newman_watts_strogatz]")
        sys.exit()

    print("--Vertices:", len(G2.nodes), "--Edges:", len(G2.edges), "\n")

    NODES = G2.number_of_nodes()
    nodes_activated = np.random.choice(NODES, NODES, replace=False)

    # Attributes to the graph
    edgeCapacities = {}
    for edge in G2.edges:
        if edge[0] == edge[1]:
            edgeCapacities[edge] = bandwidthlocalfile
        elif random.random() < 0.7:
            edgeCapacities[edge] = bandwidthWifi
        else:
            edgeCapacities[edge] = bandwidthEthernet

    print (G2.edges)

    # max-min fairness
    output = maxmin.max_min_fairness(demands=list(edgeCapacities.values()), capacity=20000000000)
    #print("OUTPUT -- max-min fairness", output)
    counter = 0
    for key, value in edgeCapacities.items():
        edgeCapacities[key] = output[counter]
        counter = counter + 1
    # print("Update", edgeCapacities)
    # End of max-min fairness

    nx.set_edge_attributes(G2, values=edgeCapacities, name='capacity')
    nx.set_edge_attributes(G2, values=0, name='usage')
    nx.set_edge_attributes(G2, values=0, name='time')
    nx.set_edge_attributes(G2, values=0, name='numImages')


    # Find the OPT solution first --------------------------------------
    # start_time_OPT = time.time()
    # res_OPT = []
    # bruteForce.vertex_cover_brute(G2, res_OPT)
    # nodes_with_image_OPT = res_OPT[0]
    # shortest_paths_OPT = nx.shortest_path(G2)
    # nearest_image_OPT = []
    # for active_node in nodes_activated:
    #     nearest_image_OPT.append(min(nodes_with_image_OPT, key=lambda x: len(shortest_paths_OPT[active_node][x])))
    # for i in range(len(nodes_activated)):
    #     sp = (shortest_paths_OPT[nodes_activated[i]][nearest_image_OPT[i]])
    #     for j in range(len(sp) - 1):
    #         G2[sp[j]][sp[j + 1]]['usage'] += imageSize
    #         G2[sp[j]][sp[j + 1]]['numImages'] = round(G2[sp[j]][sp[j + 1]]['usage'] / imageSize, 4)
    #         G2[sp[j]][sp[j + 1]]['time'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
    # print("\n", "Execution Time (OPT): %s seconds" % (time.time() - start_time_OPT))
    # print(f"nodes nodes_with_image (OPT) {nodes_with_image_OPT}")
    # print("Length of nodes with images (OPT)", len(nodes_with_image_OPT))
    # #-------------------------------------------------------------------


    start_time = time.time()

    if model == "ilp":
        ilpModel = ilp.ilp_model(G2,imageSize)
        res = ilpModel.solve()
        if res['statusCode'] == 1:
            nodes_with_image = []
            for var in res['variables']:
                if 'activation' in var.name:
                    if var.value() == 1:
                        nodes_with_image.append(int(var.name.split('_')[1]))
                else:
                    nodes = var.name.split('_')[1]+var.name.split('_')[2]
                    n = int(nodes.split(',')[0].replace('(',''))
                    d = int(nodes.split(',')[1].replace(')',''))
                    G2[n][d]['usage'] = var.value()
                    G2[n][d]['numImages'] = round(G2[n][d]['usage'] / imageSize,4)
                    G2[n][d]['time'] = round(G2[n][d]['usage'] / G2[n][d]['capacity'],6) * 100
                    print(f"Usage of channel {n} to {d} is {G2[n][d]['time']*100}")
        else:
            print(res['status'])
            return
    elif model == "approximation":
        res = []
        size_ = []
        approx.vertex_cover_approx(G2, size_, res)
        nodes_with_image = res[0]
        # print(nodes_with_image)
        shortest_paths = nx.shortest_path(G2)
        nearest_image = []
        for active_node in nodes_activated:
            nearest_image.append(min(nodes_with_image, key=lambda x: len(shortest_paths[active_node][x])))
        for i in range(len(nodes_activated)):
            sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
            print (f"Shortest Path from {nodes_activated[i]} to {nearest_image[i]} is {sp}")
            for j in range(len(sp) - 1):
                G2[sp[j]][sp[j + 1]]['usage'] +=imageSize
                G2[sp[j]][sp[j + 1]]['numImages'] = round(G2[sp[j]][sp[j + 1]]['usage'] / imageSize,4)
                G2[sp[j]][sp[j + 1]]['time'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
                print(f"Usage of channel {sp[j]} to {sp[j+1]} is {G2[sp[j]][sp[j + 1]]['time']*100}")

    elif model == "bruteforce":
        res = []
        bruteForce.vertex_cover_brute(G2, res)
        nodes_with_image = res[0]
        shortest_paths = nx.shortest_path(G2)
        nearest_image = []
        for active_node in nodes_activated:
            nearest_image.append(min(nodes_with_image, key=lambda x: len(shortest_paths[active_node][x])))
        for i in range(len(nodes_activated)):
            sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
            print(f"Shortest Path from {nodes_activated[i]} to {nearest_image[i]} is {sp}")
            for j in range(len(sp) - 1):
                G2[sp[j]][sp[j + 1]]['usage'] += imageSize
                G2[sp[j]][sp[j + 1]]['numImages'] = round(G2[sp[j]][sp[j + 1]]['usage'] / imageSize, 4)
                G2[sp[j]][sp[j + 1]]['time'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
                print(f"Usage of channel {sp[j]} to {sp[j + 1]} is {G2[sp[j]][sp[j + 1]]['time'] * 100}")

    elif model == "greedy":
        res = []
        greedy.minimum_vertex_cover_greedy(G2, res)
        nodes_with_image = res[0]
        # print(nodes_with_image)
        shortest_paths = nx.shortest_path(G2)
        nearest_image = []
        for active_node in nodes_activated:
            nearest_image.append(min(nodes_with_image, key=lambda x: len(shortest_paths[active_node][x])))
        for i in range(len(nodes_activated)):
            sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
            print(f"Shortest Path from {nodes_activated[i]} to {nearest_image[i]} is {sp}")
            for j in range(len(sp) - 1):
                G2[sp[j]][sp[j + 1]]['usage'] += imageSize
                G2[sp[j]][sp[j + 1]]['numImages'] = round(G2[sp[j]][sp[j + 1]]['usage'] / imageSize, 4)
                G2[sp[j]][sp[j + 1]]['time'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
                print(f"Usage of channel {sp[j]} to {sp[j + 1]} is {G2[sp[j]][sp[j + 1]]['time'] * 100}")

    elif model == "branchandbound":
        res = []
        branchandbound.Branch_and_Bound(G2, res)
        nodes_with_image = res[0][0]

        print (nodes_with_image)
        shortest_paths = nx.shortest_path(G2)
        nearest_image = []
        for active_node in nodes_activated:
            nearest_image.append(min(nodes_with_image, key=lambda x: len(shortest_paths[active_node][x])))
        for i in range(len(nodes_activated)):
            sp = (shortest_paths[nodes_activated[i]][nearest_image[i]])
            print(f"Shortest Path from {nodes_activated[i]} to {nearest_image[i]} is {sp}")
            for j in range(len(sp) - 1):
                G2[sp[j]][sp[j + 1]]['usage'] += imageSize
                G2[sp[j]][sp[j + 1]]['numImages'] = round(G2[sp[j]][sp[j + 1]]['usage'] / imageSize, 4)
                G2[sp[j]][sp[j + 1]]['time'] = G2[sp[j]][sp[j + 1]]['usage'] / G2[sp[j]][sp[j + 1]]['capacity']
                print(f"Usage of channel {sp[j]} to {sp[j + 1]} is {G2[sp[j]][sp[j + 1]]['time'] * 100}")

    elif model == "genetic":
        res = []
        genetic.vertex_cover_genetic(G2, res, imageSize)
        nodes_with_image = res[0]
        transfered = res[2]
        for edge in transfered:
            G2[edge[0]][edge[1]]['usage'] = transfered[edge]
            G2[edge[0]][edge[1]]['numImages'] = round(G2[edge[0]][edge[1]]['usage'] / imageSize,4)
            G2[edge[0]][edge[1]]['time'] = round(G2[edge[0]][edge[1]]['usage'] / G2[edge[0]][edge[1]]['capacity'],6) * 100
            print(f"Usage of channel {edge[0]} to {edge[1]} is {G2[edge[0]][edge[1]]['time']*100}")
    else:
        print("Give a correct model as indicated from the list\n")
        print("Available models [ilp, approximation, bruteforce, branchandbound, genetic] \n")
        sys.exit()


    # Execution Time
    print("\n","Execution Time: %s seconds" % (time.time() - start_time))
    # Nodes with image
    print(f"nodes nodes_with_image {nodes_with_image}")
    print ("Length of nodes with images", len(nodes_with_image))
    print(f"Cost function value: {getScore(G2,nodes_with_image)}")

    #print("Approximation Ratio: ", "{:.2f}".format(len(nodes_with_image) / len(nodes_with_image_OPT)))

    # print ("Length of min_weighted_vertex_cover", len(approximation.vertex_cover.min_weighted_vertex_cover(G2)))
    # approximation_ratio = "{:.2f}".format(len(nodes_with_image) / len(approximation.vertex_cover.min_weighted_vertex_cover(G2)))
    # print ("Approximation Ratio: ",approximation_ratio)

    color_map = []
    for node in G2:
        if node in nodes_with_image:
            color_map.append('green')
        else:
            color_map.append('orange')
    draw_continuum(model+"_"+graph+"_mode_"+str(2)+".png", color_map, G2, 2)
    
create_continuum()