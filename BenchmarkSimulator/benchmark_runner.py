from BenchmarkSimulator.graph_loader import GraphLoader
from GraphSearcher.congestion_factored_graph_searcher import CongestionFactoredGraphSearcher
from TrafficControl.routes_calculator import get_road_id_to_congestion

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

graph = GraphLoader.load_from('serialized_nodes.pkl', 'serialized_edges.pkl')
max_capacity = 10
max_factor = 100
congestion_factored_searcher = CongestionFactoredGraphSearcher(get_road_id_to_congestion(max_capacity, max_factor))
searcher = CongestionFactoredGraphSearcher(get_road_id_to_congestion(max_capacity, 0))
source = 27
destination = 104

for i in range(1, 5):
    path_factor = congestion_factored_searcher.find_path(graph, source, destination, None)
    path = searcher.find_path(graph, source, destination, None)
    print(f"{bcolors.OKBLUE} {path_factor}")
    print(f"{bcolors.OKGREEN} {path}")

congestion_factored_max_congestion = congestion_factored_searcher.roads_congestion.get_max_congestion()
max_congestion = searcher.roads_congestion.get_max_congestion()
print(f"{bcolors.OKBLUE} congestion_factored_max_congestion: {congestion_factored_max_congestion}")
print(f"{bcolors.OKGREEN} max_congestion: {max_congestion}")
