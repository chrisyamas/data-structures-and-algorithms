from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node

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

    def breadth_first(self, root_vertex):
        if root_vertex not in self.adj_list:
            raise KeyError
        queue = Queue()
        visited = set()
        visited.add(root_vertex)
        collection = []
        collection.append(root_vertex.value)
        # create node instance that holds vertex as its value
        first_vertex_node = Node(root_vertex)
        queue.enqueue(first_vertex_node)
        while queue.read():
            current = queue.dequeue()
            current_edges = self.adj_list[current.value]
            for edge in current_edges:
                if not self.adj_list[edge.vertex]:
                    raise KeyError
                if edge.vertex not in visited:
                    visited.add(edge.vertex)
                    collection.append(edge.vertex.value)
                    vertex_node = Node(edge.vertex)
                    queue.enqueue(vertex_node)
        print(collection)
        return(collection)

    def depth_first_search(self, start):
        def pre_order(vertex, collection=[], visited=set()):
            if not vertex or vertex not in self.adj_list or vertex in visited:
                return collection
            collection.append(vertex.value)
            visited.add(vertex)
            edge_list = self.adj_list[vertex]
            for edge in edge_list:
                pre_order(edge.vertex, collection, visited)
            return collection
        return pre_order(start)


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, neighbor, weight):
        self.vertex = neighbor
        self.weight = weight


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError
        current_front = self.front
        self.front = current_front.next
        return current_front

    def read(self):
        return self.front

    def is_empty(self):
        return not self.front
