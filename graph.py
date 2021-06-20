# Audrey Hababag  ID # 001428031

import csv


# Holds the adjacency list between all vertices and edge weights between each vertex pairs. In the case of the csv file
# provided in this project, each vertex is paired with all other vertices in the list. All edges are undirected.
class Graph:

    # Constructor
    # O(1)
    def __init__(self):
        self.adjacency = {}  # vertex dictionary {key:value}
        self.weights = {}  # edge dictionary {key:value}

    # Adds vertex to graph
    # O(1)
    def add_vertex(self, new):
        self.adjacency[new] = []

    # Adds undirected edge between vertices.
    # O(1)
    def add_edge(self, vertex_a, vertex_b, weight=1.0):
        self.weights[(vertex_a, vertex_b)] = weight
        self.weights[(vertex_b, vertex_a)] = weight


distance_data = []
graph_data = Graph()

# Extract distance data from csv file
# O(n)
with open('distance.csv') as distances:
    readCSV = csv.reader(distances)
    next(readCSV, None)
    for row in readCSV:
        distance_data.append(row)


# This function is used retrieve edge weights between vertices.
# O(n^2)
def get_weights():
    # Add vertices to the graph
    for line in distance_data:
        graph_data.add_vertex(line[1])

    # Add edges connecting the vertices
    for line in distance_data:
        for i in range(1, 28):
            graph_data.add_edge(line[0], distance_data[i - 1][0], float(line[i]))
    return graph_data.weights
