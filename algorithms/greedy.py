import timeit
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
from networkx.algorithms import approximation
from heapq import heapify, heappop
import sys

class Heap():
    # data format: [node_degree, node_index]
    heap = []
    hash = dict()

    def init(self, initial):
        self.heap = initial
        for value, index in initial:
            self.hash[index] = value
        self.rebuild()

    def rebuild(self):
        heapify(self.heap)

    def pop(self):
        return heappop(self.heap)

    def contains(self, index):
        return index in self.hash

    def update(self, index, value):
        self.hash[index] = value
        for i, e in enumerate(self.heap):
            if e[1] == index:
                self.heap[i] = [value, index]
                break
        self.rebuild()

    def get(self, index):
        return self.hash.get(index)

    def size(self):
        return len(self.heap)


def build_heap(graph):
    heap = Heap()
    degree_index = {}

    data = []  # data format: [node_degree, node_index]
    for node in graph.nodes:
        node_index = node
        degree = graph.degree[node_index]
        degree_index[node_index] = degree
        # multiply to -1 for desc order
        data.append([-1 * degree, node_index])
    heap.init(data)

    return heap, degree_index


def minimum_vertex_cover_greedy(graph, coverset):
    mvc = set()

    edges = set(graph.edges)
    heap, degrees = build_heap(graph)

    while len(edges) > 0:
        # remove node with max degree
        _, node_index = heap.pop()
        adj = set(graph.edges([node_index]))
        for u, v in adj:
            # remove edge from list
            edges.discard((u, v))
            edges.discard((v, u))

            # update neighbors
            if heap.contains(v):
                new_degree = degrees[v] - 1
                # update index
                degrees[v] = new_degree
                # update heap
                heap.update(v, -1 * new_degree)
        # add node in mvc
        mvc.add(node_index)
        coverset.append(mvc)
    return