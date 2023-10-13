import carla
import math
import random
import time

serverIP = 'localhost'
serverPort = 2000

client = carla.Client(serverIP, serverPort)
world = client.get_world()

bp_lib = world.get_blueprint_library()
map = world.get_map()
spawn_points = map.get_spawn_points()

vehicle_bp = bp_lib.find('vehicle.lincoln.mkz_2020')
vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

spectator = world.get_spectator()

for v in world.get_actors().filter('vehicle.lincoln.mkz_2020'):
    print('set autopilot true')
    v.set_autopilot(True)


def set_spectator_to(vehicle):
    transform = carla.Transform(vehicle.get_transform().transform(carla.Location(x=-8, z=2.5)),
                                vehicle.get_transform().rotation)
    spectator.set_transform(transform)


# target_location = carla.Transform(carla.Location(x=100, y=150, z=0), carla.Rotation())

for num in range(60):
    current_location = vehicle.get_location()
    print(current_location)
    set_spectator_to(vehicle)
    time.sleep(3)


print("Done")
