import carla
import math
import random
import time

serverIP = 'localhost'
serverPort = 2000

client = carla.Client(serverIP, serverPort)
world = client.get_world()

bp_lib = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()

vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020')
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

spectator = world.get_spectator()
transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-4, z=2.5)),
                            vehicle.get_transform().rotation)
spectator.set_transform(transform)

for v in world.get_actors().filter('vehicle.lincoln.mkz_2020'):
    print('set autopilot true')
    v.set_autopilot(True)

for num in range(60):
    time.sleep(1)
    print(len(world.get_actors().filter('vehicle.lincoln.mkz_2020')))



print("Done")