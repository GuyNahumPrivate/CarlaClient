from GraphSearcher.graph_searcher import GraphSearcher
import networkx as nx


class AStarGraphSearcher(GraphSearcher):
    def find_path(self, graph, source, target, heuristic, weight='length'):
        return nx.astar_path(graph, source, target, heuristic, weight)
