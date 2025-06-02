from GraphSearcher.congestion_factored_graph_searcher import CongestionFactoredGraphSearcher
from GraphSearcher.RkSP_graph_searcher import RkSPGraphSearcher
from GraphSearcher.congestion_tracking_graph_searcher_wrapper import CongestionTrackingGraphSearcherWrapper
from GraphSearcher.astar_graph_searcher import AStarGraphSearcher
from TrafficControl.routes_calculator import get_road_id_to_congestion

class SearcherProvider:

    @staticmethod
    def a_a_star_searcher(max_capacity=10):
        roads_congestion = get_road_id_to_congestion(max_capacity, 0, 0)
        return CongestionTrackingGraphSearcherWrapper(roads_congestion, AStarGraphSearcher())

    @staticmethod
    def a_congestion_factored_searcher(max_capacity=10, congestion_tolerance=0, congestion_slowdown_factor=0):
        roads_congestion = get_road_id_to_congestion(max_capacity, congestion_tolerance, congestion_slowdown_factor)
        return CongestionFactoredGraphSearcher(roads_congestion)

    @staticmethod
    def a_random_k_shortest_path_searcher(max_capacity=10):
        roads_congestion = get_road_id_to_congestion(max_capacity, 0, 0)
        return CongestionTrackingGraphSearcherWrapper(roads_congestion, RkSPGraphSearcher(k=3))
