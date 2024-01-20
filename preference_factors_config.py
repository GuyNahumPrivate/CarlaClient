from typing import Dict
from GraphSearcher.type_factored_graph_searcher import RoadType

"""
This file holds the configuration for labeling the different roads into types and the weights for each type 
based on the user preference
"""


prefer_highway: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 0.1,
    RoadType.Highway: 1
}

prefer_city: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 0.1,
    RoadType.Highway: 1
}

no_preference: Dict[RoadType, float] = {
    RoadType.Unknown: 1,
    RoadType.City: 1,
    RoadType.Highway: 1
}

user_input_to_factors: Dict[int, Dict[RoadType, float]] = {
    1: no_preference,
    2: prefer_city,
    3: prefer_highway
}


def get_road_type_factors():
    road_preference = int(input("Any road preferences? 1 - None, 2 - City, 3 - Highway \n"))
    return user_input_to_factors[road_preference]


road_id_to_type = {
    0: RoadType.City,
    2: RoadType.Highway,
    5: RoadType.Highway,
    6: RoadType.City,
    7: RoadType.City,
    9: RoadType.Highway,
    10: RoadType.Highway,
    13: RoadType.Highway,
    14: RoadType.Highway,
    16: RoadType.Highway,
    17: RoadType.Highway,
    18: RoadType.Highway,
    19: RoadType.City,
    20: RoadType.Highway,
    22: RoadType.Highway,
    33: RoadType.Highway,
    41: RoadType.Highway,
    100: RoadType.Highway,
    105: RoadType.Highway,
    254: RoadType.City,
    338: RoadType.Highway,
    395: RoadType.City,
    469: RoadType.City,
    472: RoadType.City,
    780: RoadType.City,
    787: RoadType.City,
    823: RoadType.City,
    832: RoadType.City,
    933: RoadType.Highway
}
