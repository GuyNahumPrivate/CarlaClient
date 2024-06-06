from BenchmarkSimulator.graph_loader import GraphLoader
from GraphSearcher.congestion_factored_graph_searcher import CongestionFactoredGraphSearcher
from TrafficControl.routes_calculator import get_road_id_to_congestion


graph = GraphLoader.load_from('serialized_nodes.pkl', 'serialized_edges.pkl')
max_capacity = 10
max_factor = 100
astar_searcher = CongestionFactoredGraphSearcher(get_road_id_to_congestion(max_capacity, max_factor))
source = 27
destination = 104

for i in range(1, 5):
    path = astar_searcher.find_path(graph, source, destination, None)
    print(path)

# [27, 130, 131, 123, 80, 81, 98, 104]
# [27, 22, 23, 72, 73, 76, 77, 90, 91, 81, 98, 104]
# [27, 130, 131, 123, 80, 81, 98, 104]
# [27, 22, 23, 72, 73, 76, 77, 90, 91, 81, 98, 104]

