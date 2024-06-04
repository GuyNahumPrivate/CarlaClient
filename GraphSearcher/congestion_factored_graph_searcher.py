from GraphSearcher.graph_searcher import GraphSearcher
from TrafficControl.routes_calculator import RoadCongestion
from TrafficControl.astar_modified import astar_path_with_destination

# Next Steps:
# 1. Fix persist_graph_searcher.py and make benchmark_runner.py work
# 2. run experiment that calculate the same route multiple times and see that when road is congensted the route changes

"""
This class extends a graph searcher by applying factors by roads congestion to the edge's weights
"""


class CongestionFactoredGraphSearcher(GraphSearcher):

    def __init__(self, road_id_to_congestion: dict[int, RoadCongestion]):
        self.road_id_to_congestion = road_id_to_congestion
        self.default_road_congestion = RoadCongestion(1, 0)

    def find_path(self, graph, source, target, heuristic, weight='length'):
        path = astar_path_with_destination(graph, source, target, heuristic, self._congestion_factored_weight(weight))
        self.update_congestion(path, weight, graph)

        return path

    def update_congestion(self, path, weight, graph):
        total_distance = 0
        for i in range(len(path) - 1):
            edge = graph[path[i]][path[i + 1]]
            road_id = edge['entry_waypoint'].road_id
            road_congestion = self.road_id_to_congestion[road_id]
            if road_congestion:
                road_congestion.update_congestion(total_distance, 1)

            if isinstance(weight, str):
                edge_length = edge[weight]
            else:
                edge_length = weight(path[i], path[i + 1], edge)

            total_distance += edge_length

    def _congestion_factored_weight(self, weight):
        def weight_func(edge_endpoint_1, edge_endpoint_2, edge_attributes, time):
            road_id = edge_attributes['entry_waypoint'].road_id
            road_congestion = self.road_id_to_congestion.get(road_id, self.default_road_congestion)

            if isinstance(weight, str):
                edge_weight = edge_attributes[weight]
            else:
                edge_weight = weight(edge_endpoint_1, edge_endpoint_2, edge_attributes)

            return edge_weight * road_congestion.get_congestion_factor(time)

        return weight_func
