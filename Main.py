from auto_drive_simulate import AutoDrive
from PythonAPI.carla.agents.navigation.basic_agent import BasicAgent
from carla_world_facade import connect_world, clear, create_vehicle
from preference_factors_config import road_id_to_type
from PythonAPI.carla.agents.navigation.global_route_planner import GlobalRoutePlanner
from GraphSearcher.type_factored_graph_searcher import TypeFactoredGraphSearcher
from GraphSearcher.astar_graph_searcher import AStarGraphSearcher
from GraphSearcher.congestion_factored_graph_searcher import CongestionFactoredGraphSearcher
from GraphSearcher.persist_graph_searcher import PersistGraphSearcher


def run_script(road_type_factors, target_speed, opt_dict, destination, spawn_point, debug, print_waypoints=True):
    world = connect_world()
    # clear(world)

    # Initialize agent
    graph_searcher = TypeFactoredGraphSearcher(AStarGraphSearcher(), road_type_factors, road_id_to_type)
    # graph_searcher = CongestionFactoredGraphSearcher({})
    # graph_searcher = PersistGraphSearcher(AStarGraphSearcher())
    global_route_planner = GlobalRoutePlanner(world.get_map(), 2.0, world, graph_searcher, debug)
    vehicle = create_vehicle(world, spawn_point)
    agent = BasicAgent(vehicle, target_speed=target_speed, opt_dict=opt_dict,
                       map_inst=None, grp_inst=global_route_planner)

    AutoDrive(vehicle, agent, world.get_spectator()) \
        .start_game_loop(destination, set_random_destination_on_complete=False, auto_adjust_spectator=False, debug=print_waypoints)
