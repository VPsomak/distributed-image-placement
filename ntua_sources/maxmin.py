import networkx as nx
import numpy as np
import random
import numpy.random

random.seed(10)
numpy.random.seed(10)
imageSize = 3*1024*1024*1024

# # 10.737.418.240
# bandwidthEthernet = 10*1024*1024*1024
# # 26214400
# bandwidthWifi = 25*1024*1024
# # 524288
# bandwidthlocalfile = 0.5*1024*1024

# http://www.mathcs.emory.edu/~cheung/Courses/558/Syllabus/11-Fairness/Fair.html

def max_min_fairness(demands, capacity):
    capacity_remaining = capacity
    output = []

    for i, demand in enumerate(demands):
        share = capacity_remaining / (len(demands) - i)
        allocation = min(share, demand)

        if i == len(demands) - 1:
            allocation = max(share, capacity_remaining)

        output.append(allocation)
        capacity_remaining -= allocation

    return output


# tests = [
#     (dict(demands=[1, 1], capacity=20), [1, 19]),
#     (dict(demands=[2, 8], capacity=10), [2, 8]),
#     (dict(demands=[2, 8], capacity=5), [2, 3]),
#     (dict(demands=[1, 2, 5, 10], capacity=20), [1, 2, 5, 12]),
#     (dict(demands=[2, 2.6, 4, 5], capacity=10), [2, 2.6, 2.7, 2.7]),
# ]

# G2 = nx.barabasi_albert_graph(50, 8)
# edgeCapacities = {}
# for edge in G2.edges:
#     if edge[0] == edge[1]:
#         edgeCapacities[edge] = bandwidthlocalfile
#     elif random.random() < 0.7:
#         edgeCapacities[edge] = bandwidthWifi
#     else:
#         edgeCapacities[edge] = bandwidthEthernet
#
# print (edgeCapacities)
# # print (list(edgeCapacities.values()))
# # print ("\n\n")
#
# output = max_min_fairness(demands=list(edgeCapacities.values()), capacity=20737418240)
# # output  = max_min_fairness(demands=[1, 2, 5, 10], capacity=20)
# print("OUTPUT -- max-min fairness", output)
#
# counter = 0
# for key, value in edgeCapacities.items():
#     edgeCapacities[key] = output[counter]
#     counter = counter +1
# print ("Update", edgeCapacities)
