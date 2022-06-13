# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge

This module implements a Graph. The graph is represented as an adjacency list, and includes the following methods:

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Approach & Efficiency

The module includes a Graph, Vertex, and Edge class respectively.

### Graph class

The adjacency list is a class attribute of Graph, in the form of a hashtable (or dictionary).

The add_node() method takes an input value, creates a new instance of Vertex with the input value, and adds that new node/vertex as a key in the adjacency list hashtable with its corresponding value being an empty list.

The add_edge() method takes as its arguments two nodes (node_a and node_b) and an optional weight input (with None default value). If either of the nodes are not present in the adjancency list hashtable, a KeyError is raised. Otherwise, a new instance of Edge is created with the node_b and weight arguments, and that new Edge is appended to the list that exists as the value paired with node_a as the key in the Graph's adjacency list hashtable.

The get_nodes() method accesses all of the nodes in the graph as keys in the adjacency list hashtable, and returns them in the form of a list.

The get_neighbors() method takes a node and accesses the value paired with that node key in the adjacency list hashtable. The value is the list of all edges starting from that vertex. That list is returned by the method.

The size() method returns the length of the adjacency list, which is by design always equal to the number of nodes in the graph.
