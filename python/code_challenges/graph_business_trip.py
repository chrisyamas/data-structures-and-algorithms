from data_structures.graph import Graph


def direct_flights(network, trip_array):
    total_cost = 0
    adj_cities = {}
    for city, edges in network.adj_list.items():
        new_edges = {}
        for edge in edges:
            new_edges[edge.vertex.value] = edge.weight
        adj_cities[city.value] = new_edges
    for i in range(1, len(trip_array)):
        origin = trip_array[i-1]
        destination = trip_array[i]
        if origin not in adj_cities or destination not in adj_cities[origin]:
            return (False, 0)
        flight_cost = adj_cities[origin][destination]
        total_cost += flight_cost
    return (True, total_cost)
