class RoadCongestion:

    def __init__(self, max_capacity, max_factor):
        self.max_capacity = max_capacity
        self.max_factor = max_factor

        # In the current implementation we will assume relative time, it might change to exact time
        self.time_to_congest = {}

    def get_congestion_factor(self, time):
        congestion_level = min(self.time_to_congest.get(time, 0) / self.max_capacity, 1)
        congestion_factor = 1 + congestion_level * self.max_factor
        return congestion_factor

    def update_congestion(self, time, congestion):
        self.time_to_congest[time] = self.time_to_congest.get(time, 0) + congestion


# class CongestionManager:
#
#     def __init__(self, road_id_to_congestion: nx.DiGraph):
#         self.road_id_to_congestion = create_road_congestion(graph)
#
#
#     def create_road_congestion(self, graph: nx.DiGraph):
#         road_id_to_congestion = {}
#         for edge in graph.edges:
#             road_id = graph[edge[0]][edge[1]]['road_id']
#             road_id_to_congestion[road_id] = RoadCongestion(graph[edge[0]][edge[1]]['weight'], 100, 10)
#         return road_id_to_congestion
#     #self.graph = graph
#
#
#     def calculate(self, start, end):
#         # some code
#         return routes