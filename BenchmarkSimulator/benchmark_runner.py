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


def a_searcher(max_capacity=10, congestion_tolerance=0, congestion_slowdown_factor=0):
    roads_congestion = get_road_id_to_congestion(max_capacity, congestion_tolerance, congestion_slowdown_factor)
    return CongestionFactoredGraphSearcher(roads_congestion)


# The higher the factor will be, the less the congestion level will be and the average travel time will be higher:
print("\ndifferent congestion_tolerance")

print("\nRunning with congestion_tolerance: 100\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))
# factored_congestion_level: 2.5
# factored_average_travel_time: 140.08
# congestion_level: 5.0
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning with congestion_tolerance: 50\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=50))
# factored_congestion_level: 26
# factored_average_travel_time: 136.92
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning with congestion_tolerance: 10\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=10))
# factored_congestion_level: 28
# factored_average_travel_time: 123.12
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 2.272727272727273

print("\nRunning with congestion_tolerance: 5\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=5))

print("\nRunning with congestion_tolerance: 0\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=0))

# The more load on the roads,
# we might reach the limit of the traffic distribution, and the congestion level improvement will decrease
print("\ndifferent loads\n")

print("\nRunning with load: 50\n")
benchmark.run(graph, source, destination, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))
# factored_congestion_level: 25
# factored_average_travel_time: 140.08
# congestion_level: 50
# average_travel_time: 88.0
# upper_bound: 3.590909090909091

print("\nRunning with load: 150\n")
benchmark.run(graph, source, destination, 150, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))
# factored_congestion_level: 87
# factored_average_travel_time: 181.84666666666666
# congestion_level: 150
# average_travel_time: 88.0
# upper_bound: 5.875

print("\nRunning with load: 500\n")
benchmark.run(graph, source, destination, 500, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))
# factored_congestion_level: 413
# factored_average_travel_time: 116.154
# congestion_level: 500
# average_travel_time: 88.0
# upper_bound: 5.875

print("\nRunning with load: 1500\n")
benchmark.run(graph, source, destination, 1500, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))

# depends on the graph, we might get improvements without effecting the average travel time:
print("\n different graphs \n")

# Add edges to the graph so the path will have exactly 2 path from node 1 to node 10 with even length
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
even_graph = nx.DiGraph()

for i in range(1, 11):
    even_graph.add_node(i)

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

print("\nRunning even graph\n")
benchmark.run(even_graph, 1, 10, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))

# Add edges to the graph, so it will have exactly 2 path from node 1 to node 6 with different length
#             1
#            / \
#           2   |
#           |   |
#           3   |
#      1    |   |    2
#           4   |
#           |   |
#           5   |
#            \ /
#             6
two_path_graph = nx.DiGraph()

for i in range(1, 7):
    even_graph.add_node(i)

two_path_graph.add_edge(1, 2, length=100, entry_waypoint=EntryWaypoint(1))
two_path_graph.add_edge(2, 3, length=100, entry_waypoint=EntryWaypoint(1))
two_path_graph.add_edge(3, 4, length=100, entry_waypoint=EntryWaypoint(1))
two_path_graph.add_edge(4, 5, length=100, entry_waypoint=EntryWaypoint(1))
two_path_graph.add_edge(5, 6, length=100, entry_waypoint=EntryWaypoint(1))
two_path_graph.add_edge(1, 6, length=1, entry_waypoint=EntryWaypoint(2))

print("\nRunning two paths graph\n")
benchmark.run(two_path_graph, 1, 6, 50, a_searcher(), a_searcher(max_capacity=10, congestion_tolerance=100))
