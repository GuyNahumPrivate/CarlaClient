from auto_drive_simulate import AutoDrive
from PythonAPI.carla.agents.navigation.basic_agent import BasicAgent
from carla import Location
from carla_world_facade import connect_world, clear, create_vehicle
from preference_factors_config import get_road_type_factors, road_id_to_type
from PythonAPI.carla.agents.navigation.global_route_planner import GlobalRoutePlanner
from GraphSearcher.type_factored_graph_searcher import TypeFactoredGraphSearcher
from GraphSearcher.astar_graph_searcher import AStarGraphSearcher
import carla

world = connect_world()
clear(world)
destination = Location(x=6.006511, y=66.283257, z=0.600000)
spawn_point = carla.Transform(carla.Location(x=0.445544, y=13.185217, z=0.600000),
                              carla.Rotation(pitch=360, yaw=-179.840790, roll=0))

# Initialize agent
road_type_factors = get_road_type_factors()
graph_searcher = TypeFactoredGraphSearcher(AStarGraphSearcher(), road_type_factors, road_id_to_type)
global_route_planner = GlobalRoutePlanner(world.get_map(), 2.0, world, graph_searcher)
vehicle = create_vehicle(world, spawn_point)
agent = BasicAgent(vehicle, target_speed=40, opt_dict={'ignore_traffic_lights': True, 'ignore_stop_signs': True}, map_inst=None, grp_inst=global_route_planner)

AutoDrive(vehicle, agent, world.get_spectator())\
    .start_game_loop(destination, set_random_destination_on_complete=False, auto_adjust_spectator=False)
