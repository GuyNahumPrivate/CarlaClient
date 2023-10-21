from BenchmarkSimulator.graph_loader import GraphLoader
from GraphSearcher.astar_graph_searcher import AStarGraphSearcher
from BenchmarkSimulator.heuristic_func_helper import HeuristicHelper

graph = GraphLoader.load_from('serialized_nodes.pkl', 'serialized_edges.pkl')
astar_searcher = AStarGraphSearcher()

#todo: inject heuristic function
result = astar_searcher.find_path(graph, 123, 3, None)