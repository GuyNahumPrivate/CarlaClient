from typing import Dict
from GraphSearcher.type_factored_graph_searcher import RoadType

"""
This file holds the configuration for labeling the different roads into types and the weights for each type 
based on the user preference
"""


prefer_highway_factors: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 10,
    RoadType.Highway: 1
}

prefer_city_factors: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 0.1,
    RoadType.Highway: 1
}

no_preference_factors: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 1,
    RoadType.Highway: 1
}

user_input_to_factors: Dict[int, Dict[RoadType, float]] = {
    1: no_preference_factors,
    2: prefer_city_factors,
    3: prefer_highway_factors
}


def get_road_type_factors():
    road_preference = int(input("Any road preferences? 1 - None, 2 - City, 3 - Highway \n"))
    return user_input_to_factors[road_preference]


# Labeling of road ids to types
road_id_to_type: dict[int, RoadType] = {
    11: RoadType.City,
    12: RoadType.City,
    18: RoadType.City,
    19: RoadType.City,
    20: RoadType.City,
    21: RoadType.City,
    256: RoadType.City,
    268: RoadType.City,
    382: RoadType.City,
    395: RoadType.City,
}
