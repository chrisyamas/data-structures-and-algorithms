
class Graph:

    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        new_node = Vertex(value)
        self.adj_list[new_node] = []
        return new_node

    def add_edge(self, node_a, node_b, weight=None):
        if node_a not in self.adj_list or node_b not in self.adj_list:
            raise KeyError
        new_edge = Edge(node_b, weight)
        edge_list = self.adj_list[node_a]
        edge_list.append(new_edge)

    def get_nodes(self):
        node_list = list(self.adj_list.keys())
        return node_list

    def get_neighbors(self, node):
        node_neighbors = self.adj_list[node]
        return node_neighbors

    def size(self):
        return len(self.adj_list)


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, neighbor, weight):
        self.vertex = neighbor
        self.weight = weight

