import carla
from vehicle_builder import VehicleBuilder
from auto_drive_simulate import AutoDrive
from PythonAPI.carla.agents.navigation.basic_agent import BasicAgent

serverIP = 'localhost'
serverPort = 2000

client = carla.Client(serverIP, serverPort)
world = client.get_world()
spawn_points = world.get_map().get_spawn_points()
bp_lib = world.get_blueprint_library()

spectator = world.get_spectator()
vehicle = VehicleBuilder().a_vehicle(world)
agent = BasicAgent(vehicle)

AutoDrive(vehicle, agent, spectator, spawn_points).start_game_loop()
