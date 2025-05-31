from typing import Dict


class RoadCongestion:

    def __init__(self, max_capacity, congestion_tolerance, traffic_slowdown_factor=1.0):
        self.max_capacity = max_capacity
        self.congestion_tolerance = congestion_tolerance
        self.traffic_slowdown_factor = traffic_slowdown_factor

        # In the current implementation we will assume relative time, it might change to exact time
        self.time_to_congest = {}

    def calculate_factor(self, time, factor):
        # todo: round the time according to the defined time intervals
        congestion_level = self.time_to_congest.get(time, 0) / self.max_capacity
        return 1 + congestion_level * factor

    def get_congestion_tolerance_factor(self, time):
        return self.calculate_factor(time, self.congestion_tolerance)

    def get_traffic_slowdown_factor(self, time):
        return self.calculate_factor(time, self.traffic_slowdown_factor)

    def update_congestion(self, time, congestion):
        self.time_to_congest[int(time)] = self.time_to_congest.get(time, 0) + congestion


class RoadsCongestion:

    def __init__(self, road_id_to_congestion: Dict[int, RoadCongestion]):
        self.road_id_to_congestion = road_id_to_congestion
        self.default_road_congestion = RoadCongestion(1, 0)

    def get_congestion_factor(self, road_id, time):
        return self.road_id_to_congestion\
            .get(road_id, self.default_road_congestion)\
            .get_congestion_tolerance_factor(time)

    def get_traffic_slowdown_factor(self, road_id, time):
        return self.road_id_to_congestion \
            .get(road_id, self.default_road_congestion) \
            .get_traffic_slowdown_factor(time)

    def update_congestion(self, path, weight, graph):
        total_distance = 0
        for i in range(len(path) - 1):
            edge = graph[path[i]][path[i + 1]]
            road_id = edge['entry_waypoint'].road_id
            road_congestion = self.road_id_to_congestion.get(road_id)
            if road_congestion:
                road_congestion.update_congestion(total_distance, 1)

            if isinstance(weight, str):
                edge_length = edge[weight]
            else:
                edge_length = weight(path[i], path[i + 1], edge)

            factor = self.get_congestion_factor(road_id, total_distance)
            total_distance += (edge_length * factor)

        return total_distance

    def get_max_congestion(self):
        max_congestion = 0
        for road_congestion in self.road_id_to_congestion.values():
            if len(road_congestion.time_to_congest.values()) > 0:
                capacity = road_congestion.max_capacity
                max_vehicles = max(road_congestion.time_to_congest.values())
                max_congestion = max(max_congestion, max_vehicles / capacity)
        return max_congestion


road_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 33, 41, 89, 90, 100, 105, 125, 150, 151, 152, 160, 172, 179, 254, 255, 256, 268, 286, 296, 315, 338, 344, 375, 382, 395, 466, 467, 469, 472, 476, 486, 515, 516, 565, 566, 579, 584, 597, 608, 630, 637, 655, 675, 676, 703, 712, 735, 736, 763, 780, 787, 795, 801, 811, 823, 832, 843, 848, 875, 876, 900, 933, 934, 939]


def get_road_id_to_congestion(max_capacity, congestion_tolerance, traffic_slowdown_factor):
    road_id_to_congestion = {}

    for road_id in road_ids:
        road_id_to_congestion[road_id] = RoadCongestion(max_capacity, congestion_tolerance, traffic_slowdown_factor)

    return RoadsCongestion(road_id_to_congestion)

