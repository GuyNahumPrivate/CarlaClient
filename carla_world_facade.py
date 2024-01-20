import carla
import random

"""
This facade simplifies the operation that can be done in Carla World. 
"""


def connect_world(server_ip='localhost', server_port=2000):
    client = carla.Client(server_ip, server_port)
    return client.get_world()


def clear(world: carla.World):
    actors = world.get_actors()

    # Iterate through actors and remove vehicles
    for actor in actors:
        if 'vehicle' in actor.type_id:
            actor.destroy()


def create_vehicle(world: carla.World, spawn_point, vehicle_model='vehicle.lincoln.mkz_2020'):
    print("vehicle spawn point:", spawn_point)
    bp_lib = world.get_blueprint_library()
    vehicle_bp = bp_lib.find(vehicle_model)

    return world.try_spawn_actor(vehicle_bp, spawn_point)


def get_random_spawn_point(world: carla.World):
    spawn_points = world.get_map().get_spawn_points()
    return random.choice(spawn_points)
