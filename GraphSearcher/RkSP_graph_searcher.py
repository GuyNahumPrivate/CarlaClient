from GraphSearcher.graph_searcher import GraphSearcher
import networkx as nx
import random
from itertools import islice

"""
       Find k different shortest paths between source and target nodes using NetworkX's k_shortest_paths.
       Randomly selects one of the k paths to return.
       
       Parameters
       ----------
       graph : nx.DiGraph
           The directed graph to search in
       source : node
           Starting node for path
       target : node
           Ending node for path
       heuristic : function
           Heuristic function (not used in this implementation)
       weight : string or function
           Edge weight attribute or function
           
       Returns
       -------
       list
           A list of nodes representing one of the k shortest paths
       """
class RkSPGraphSearcher(GraphSearcher):
    def __init__(self, k=3):
        self.k = k

    def find_path(self, graph: nx.DiGraph, source, target, heuristic, weight='length'):
        shortest_paths = nx.shortest_simple_paths(graph, source, target, weight=weight)
        paths = list(islice(shortest_paths, self.k))
        selected_path = random.choice(paths)

        return selected_path

