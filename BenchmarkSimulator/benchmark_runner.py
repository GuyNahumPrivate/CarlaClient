from BenchmarkSimulator.graph_loader import GraphLoader, EntryWaypoint
from GraphSearcher.congestion_factored_graph_searcher import CongestionFactoredGraphSearcher
from TrafficControl.routes_calculator import get_road_id_to_congestion
from BenchmarkSimulator.single_src_dest_benchmark import SingleSrcDestBenchmark
import networkx as nx

graph = GraphLoader.load_from('serialized_nodes.pkl', 'serialized_edges.pkl')
print(graph)
source = 27
destination = 104
benchmark = SingleSrcDestBenchmark()


def a_searcher(max_capacity=10, max_factor=0):
    return CongestionFactoredGraphSearcher(get_road_id_to_congestion(max_capacity, max_factor))


# The higher the factor will be, the less the congestion level will be and the average travel time will be higher:

print("\nRunning benchmark with max_capacity=10, max_factor=100\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, max_factor=100))
# factored_congestion_level: 25
# factored_average_travel_time: 140.08
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning benchmark with max_capacity=10, max_factor=10 \n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, max_factor=50))
# factored_congestion_level: 26
# factored_average_travel_time: 136.92
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning benchmark with max_capacity=10, max_factor=100, total_path_calculation=150 \n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, max_factor=10))
# factored_congestion_level: 28
# factored_average_travel_time: 123.12
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 2.272727272727273


# The more load on the roads,
# we might reach the limit of the traffic distribution, and the congestion level improvement will decrease

print("\nRunning benchmark with 50 paths, max_capacity=10, max_factor=100\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, max_factor=100))
# factored_congestion_level: 25
# factored_average_travel_time: 140.08
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning benchmark with 150 paths, max_capacity=10, max_factor=10 \n")
benchmark.run(graph, source, destination, 150, a_searcher(), a_searcher(max_capacity=10, max_factor=100))
# factored_congestion_level: 87
# factored_average_travel_time: 181.84666666666666
# congestion_level: 150
# average_travel_time: 88.0
# upper_bound: 5.875

print("\nRunning benchmark with paths =500, max_capacity=10, max_factor=100 \n")
benchmark.run(graph, source, destination, 500, a_searcher(), a_searcher(max_capacity=10, max_factor=100))
# factored_congestion_level: 413
# factored_average_travel_time: 116.154
# congestion_level: 500
# average_travel_time: 88.0
# upper_bound: 5.875


# depends on the graph, we might get improvements without effecting the average travel time:
even_graph = nx.DiGraph()
# # add edges to the graph so the path will have exactly 2 path from node 1 to node 10 with even length
#             1
#            / \
#           2   6
#           |   |
#           3   7
#      1    |   |    2
#           4   8
#           |   |
#           5   9
#            \ /
#            10
# add nodes to the graph
for i in range(1, 11):
    even_graph.add_node(i)

# add edges to the graph

even_graph.add_edge(1, 2, length=1, entry_waypoint=EntryWaypoint(1))
even_graph.add_edge(2, 3, length=1, entry_waypoint=EntryWaypoint(1))
even_graph.add_edge(3, 4, length=1, entry_waypoint=EntryWaypoint(1))
even_graph.add_edge(4, 5, length=1, entry_waypoint=EntryWaypoint(1))
even_graph.add_edge(5, 10, length=1, entry_waypoint=EntryWaypoint(1))
even_graph.add_edge(1, 6, length=1, entry_waypoint=EntryWaypoint(2))
even_graph.add_edge(6, 7, length=1, entry_waypoint=EntryWaypoint(2))
even_graph.add_edge(7, 8, length=1, entry_waypoint=EntryWaypoint(2))
even_graph.add_edge(8, 9, length=1, entry_waypoint=EntryWaypoint(2))
even_graph.add_edge(9, 10, length=1, entry_waypoint=EntryWaypoint(2))

print("\nRunning benchmark with on even graph max_capacity=10, max_factor=100 \n")
benchmark.run(even_graph, 1, 10, 50, a_searcher(), a_searcher(max_capacity=10, max_factor=100))