from GraphSearcher.graph_searcher import GraphSearcher
from TrafficControl.astar_modified import astar_path_with_destination
from TrafficControl.routes_calculator import RoadsCongestion

"""
This class extends a graph searcher by applying factors by roads congestion to the edge's weights
"""


class CongestionFactoredGraphSearcher(GraphSearcher):

    def __init__(self, roads_congestion: RoadsCongestion):
        self.roads_congestion = roads_congestion

    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = astar_path_with_destination(graph, source, target, heuristic, self._congestion_factored_weight(weight))
        self.roads_congestion.update_congestion(path, weight, graph)

        return path

    def _congestion_factored_weight(self, weight):
        def weight_func(edge_endpoint_1, edge_endpoint_2, edge_attributes, time):
            road_id = edge_attributes['entry_waypoint'].road_id
            road_congestion = self.roads_congestion.get(road_id)

            if isinstance(weight, str):
                edge_weight = edge_attributes[weight]
            else:
                edge_weight = weight(edge_endpoint_1, edge_endpoint_2, edge_attributes)

            return edge_weight * road_congestion.get_congestion_factor(time)

        return weight_func

