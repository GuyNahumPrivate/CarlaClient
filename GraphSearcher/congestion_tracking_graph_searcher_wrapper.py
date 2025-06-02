from GraphSearcher.graph_searcher import GraphSearcher
from TrafficControl.routes_calculator import RoadsCongestion

"""
This class extends a graph searcher by applying factors by roads congestion to the edge's weights
"""


class CongestionTrackingGraphSearcherWrapper(GraphSearcher):

    def __init__(self, roads_congestion: RoadsCongestion, searcher: GraphSearcher):
        self.roads_congestion = roads_congestion
        self.searcher = searcher

    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = self.searcher.find_path(graph, source, target, heuristic, weight)
        self.roads_congestion.update_congestion(path, weight, graph)

        return path
