import networkx as nx
import numpy as np
from random import randint, uniform, choice, shuffle
import matplotlib.pyplot as plt
from networkx.algorithms import approximation

# global configuration settings
# note: keep population_size and elite_population_size of same parity
population_size = 30
elite_population_size = 8
mutation_probability = 0.04
num_iterations = 5

# a weighted choice function
def weighted_choice(choices, weights):
    normalized_weights = np.array([weight for weight in weights]) / np.sum(weights)
    threshold = uniform(0, 1)
    total = 1
    for index, normalized_weight in enumerate(normalized_weights):
        total -= normalized_weight
        if total < threshold:
            return choices[index]

# Vertex Cover class definition
class VertexCover:
    def __init__(self, associated_population=None):
        # population to which this point belongs
        self.associated_population = associated_population

        # randomly create chromosome
        self.chromosomes = [randint(0, 1) for _ in range(len(self.associated_population.graph.nodes()))]

        # initialize
        self.vertexarray = np.array([False for _ in range(len(self.associated_population.graph.nodes()))])
        self.chromosomenumber = 0
        self.vertexlist = np.array([])

        # required when considering the entire population
        self.index = -1
        self.fitness = 0.0
        self.diversity = 0.0
        self.fitness_rank = -1
        self.diversity_rank = -1
        self.evaluated_fitness = False

    def evaluate_fitness(self):
        if not self.evaluated_fitness:
            original_graph = self.associated_population.graph.copy()

            self.vertexarray = np.array([False for _ in range(len(original_graph.nodes()))])
            self.chromosomenumber = 0

            while len(original_graph.edges) > 0:
                # shuffle the list of vertices
                node_list = list(original_graph.nodes)
                shuffle(node_list)

                # remove all degree-1 vertices one-by-one
                degree_one_vertex_found = False
                for vertex in node_list:
                    if original_graph.degree[vertex] == 1:
                        degree_one_vertex_found = True

                        neighbors = list(original_graph.neighbors(vertex))
                        adjvertex = neighbors[0]

                        # select the adjacent vertex
                        self.vertexarray[adjvertex] = True

                        # remove vertex along with neighbours from graph
                        removed_subgraph = neighbors
                        removed_subgraph.append(vertex)
                        original_graph.remove_nodes_from(removed_subgraph)

                        break

                # no more degree-1 vertices left
                if not degree_one_vertex_found:
                    # randomly choose one of the remaining vertices
                    vertex = choice(list(original_graph.nodes))
                    if original_graph.degree[vertex] >= 2:
                        # make a choice depending on the chromosome bit
                        if self.chromosomes[self.chromosomenumber] == 0:
                            # add all neighbours to vertex cover
                            for othervertex in original_graph.neighbors(vertex):
                                self.vertexarray[othervertex] = True

                            # remove vertex along with neighbours from graph
                            removed_subgraph = list(original_graph.neighbors(vertex))
                            removed_subgraph.append(vertex)
                            original_graph.remove_nodes_from(removed_subgraph)

                        elif self.chromosomes[self.chromosomenumber] == 1:
                            # add only this vertex to the vertex cover
                            self.vertexarray[vertex] = True

                            # remove only this vertex from the graph
                            original_graph.remove_node(vertex)

                        # go to the next chromosome to be checked
                        self.chromosomenumber = self.chromosomenumber + 1
                        continue

            # put all true elements in a numpy array - representing the actual vertex cover
            self.vertexlist = np.where(self.vertexarray == True)[0]
            self.fitness = len(self.associated_population.graph.nodes()) / (1 + len(self.vertexlist))
            self.evaluated_fitness = True

        return self.fitness

    # mutate the chromosome at a random index
    def mutate(self):
        if self.chromosomenumber > 0:
            index = randint(0, self.chromosomenumber)
        else:
            index = 0

        if self.chromosomes[index] == 0:
            self.chromosomes[index] = 1
        elif self.chromosomes[index] == 1:
            self.chromosomes[index] = 0

        self.evaluated_fitness = False
        self.evaluate_fitness()

    def __len__(self):
        return len(self.vertexlist)

    def __iter__(self):
        return iter(self.vertexlist)

# class for the 'population' of vertex covers
class Population:
    def __init__(self, G, size):
        self.vertexcovers = []
        self.size = size
        self.graph = G.copy()

        for vertex_cover_number in range(self.size):
            vertex_cover = VertexCover(self)
            vertex_cover.evaluate_fitness()

            self.vertexcovers.append(vertex_cover)
            self.vertexcovers[vertex_cover_number].index = vertex_cover_number

        self.evaluated_fitness_ranks = False
        self.evaluated_diversity_ranks = False
        self.mean_fitness = 0
        self.mean_diversity = 0
        self.mean_vertex_cover_size = 0
        self.average_vertices = np.zeros((len(self.graph.nodes()), 1))

    # evaluate fitness ranks for each vertex cover
    def evaluate_fitness_ranks(self):
        if not self.evaluated_fitness_ranks:
            for vertex_cover in self.vertexcovers:
                vertex_cover.fitness = vertex_cover.evaluate_fitness()
                self.mean_fitness += vertex_cover.fitness
                self.mean_vertex_cover_size += len(vertex_cover)

            self.mean_fitness /= self.size
            self.mean_vertex_cover_size /= self.size
            self.vertexcovers.sort(key=lambda vertex_cover: vertex_cover.fitness, reverse=True)

            for rank_number in range(self.size):
                self.vertexcovers[rank_number].fitness_rank = rank_number

            self.evaluated_fitness_ranks = True

    # evaluate diversity rank of each point in population
    def evaluate_diversity_ranks(self):
        if not self.evaluated_diversity_ranks:
            # find the average occurrence of every vertex in the population
            for vertex_cover in self.vertexcovers:
                self.average_vertices[vertex_cover.vertexlist] += 1

            self.average_vertices /= self.size

            for vertex_cover in self.vertexcovers:
                vertex_cover.diversity = np.sum(np.abs(vertex_cover.vertexlist - self.average_vertices))/self.size
                self.mean_diversity += vertex_cover.diversity

            self.mean_diversity /= self.size
            self.vertexcovers.sort(key=lambda vertex_cover: vertex_cover.diversity, reverse=True)

            for rank_number in range(self.size):
                self.vertexcovers[rank_number].diversity_rank = rank_number

            self.evaluated_diversity_ranks = True

    # generate the new population by breeding vertex covers
    def breed(self):
        # sort according to fitness_rank
        self.vertexcovers.sort(key=lambda vertex_cover: vertex_cover.fitness_rank)

        # push all the really good ('elite') vertex covers first
        newpopulation = []
        for index in range(elite_population_size):
            newpopulation.append(self.vertexcovers[index])

        # assign weights to being selected for breeding
        weights = [1 / (1 + vertex_cover.fitness_rank + vertex_cover.diversity_rank) for vertex_cover in self.vertexcovers]

        # randomly select for the rest and breed
        while len(newpopulation) < population_size:
            parent1 = weighted_choice(list(range(population_size)), weights)
            parent2 = weighted_choice(list(range(population_size)), weights)

            # don't breed with yourself, dude!
            while parent1 == parent2:
                parent1 = weighted_choice(list(range(population_size)), weights)
                parent2 = weighted_choice(list(range(population_size)), weights)

            # breed now
            child1, child2 = crossover(self.vertexcovers[parent1], self.vertexcovers[parent2])

            # add the children
            newpopulation.append(child1)
            newpopulation.append(child2)

        # assign the new population
        self.vertexcovers = newpopulation

        self.evaluated_fitness_ranks = False
        self.evaluated_diversity_ranks = False

    # mutate population randomly
    def mutate(self):
        for vertex_cover in self.vertexcovers:
            test_probability = uniform(0, 1)
            if test_probability < mutation_probability:
                vertex_cover.mutate()
                vertex_cover.evaluate_fitness()

                self.evaluated_fitness_ranks = False
                self.evaluated_diversity_ranks = False


# crossover between two vertex cover chromosomes
def crossover(parent1, parent2):
    if parent1.associated_population != parent2.associated_population:
        raise ValueError("Vertex covers belong to different populations.")
    child1 = VertexCover(parent1.associated_population)
    child2 = VertexCover(parent2.associated_population)
    # find the point to split and rejoin the chromosomes
    # note that chromosome number + 1 is the actual length of the chromosome in each vertex cover encoding
    split_point = randint(0, min(parent1.chromosomenumber, parent2.chromosomenumber))
    # actual splitting and recombining
    child1.chromosomes = parent1.chromosomes[:split_point] + parent2.chromosomes[split_point:]
    child2.chromosomes = parent2.chromosomes[:split_point] + parent1.chromosomes[split_point:]
    # evaluate fitnesses
    child1.evaluate_fitness()
    child2.evaluate_fitness()
    return child1, child2

def vertex_cover_genetic(G, population_size):
    # initialise vertex cover population
    population = Population(G, population_size)
    population.evaluate_fitness_ranks()
    population.evaluate_diversity_ranks()

    # for plotting
    plot_fitness = [population.mean_fitness]
    plot_diversity = [population.mean_diversity]

    # breed and mutate this population num_iterations times
    for iteration in range(1, num_iterations + 1):
        population.breed()
        population.mutate()
        # find the new ranks
        population.evaluate_fitness_ranks()
        population.evaluate_diversity_ranks()
        # add to the plot
        plot_fitness.append(population.mean_fitness)
        plot_diversity.append(population.mean_diversity)

    # vertex cover with best fitness is our output
    best_vertex_cover = None
    best_fitness = 0
    for vertex_cover in population.vertexcovers:
        if vertex_cover.fitness > best_fitness:
            best_vertex_cover = vertex_cover

    # print("Best Vertex Cover Size =", len(best_vertex_cover))
    # print("Best Vertex Cover = ", best_vertex_cover.vertexlist)
    # # print("approximation=", len(approximation.min_weighted_vertex_cover(G)))
    # print ("approximation ratio", len(best_vertex_cover)/len(approximation.min_weighted_vertex_cover(G)))
