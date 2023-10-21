import numpy as np


class HeuristicHelper:

    def __init__(self, graph):
        self.graph = graph

    def distance_heuristic(self, n1, n2):
        """
        Distance heuristic calculator for path searching
        in self._graph
        """
        l1 = np.array(self.graph.nodes[n1]['vertex'])
        l2 = np.array(self.graph.nodes[n2]['vertex'])
        return np.linalg.norm(l1-l2)
