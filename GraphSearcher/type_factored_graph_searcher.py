from GraphSearcher.graph_searcher import GraphSearcher
from enum import Enum
from typing import Dict


class RoadType(Enum):
    Unknown = 0
    City = 1
    Highway = 2


"""
This class extends a graph searcher by applying factors by types to the edge's weights
"""


class TypeFactoredGraphSearcher(GraphSearcher):
    def __init__(self, searcher: GraphSearcher, road_type_to_factor: Dict[RoadType, float], road_id_to_type):
        self.searcher = searcher
        self.road_type_to_factor = road_type_to_factor
        self.road_id_to_type = road_id_to_type

    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = self.searcher.find_path(graph, source, target, heuristic, self._type_factored_weight(weight))
        print('path', path)

        return path

    def _type_factored_weight(self, weight):
        def weight_func(edge_endpoint_1, edge_endpoint_2, edge_attributes):
            road_id = edge_attributes['entry_waypoint'].road_id
            road_type = self.road_id_to_type.get(road_id, RoadType.Unknown)
            weight_factor = self.road_type_to_factor.get(road_type, 1)

            if isinstance(weight, str):
                return edge_attributes[weight] * weight_factor
            else:
                return weight(edge_endpoint_1, edge_endpoint_2, edge_attributes) * weight_factor

        return weight_func
