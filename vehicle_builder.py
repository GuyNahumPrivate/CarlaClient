import carla
import random


class VehicleBuilder:
    vehicle_model = 'vehicle.lincoln.mkz_2020'

    def a_vehicle(self, world: carla.World):
        map = world.get_map()
        bp_lib = world.get_blueprint_library()
        vehicle_bp = bp_lib.find(self.vehicle_model)
        vehicle_spawn_point = self.get_spawn_point(map.get_spawn_points())

        return world.try_spawn_actor(vehicle_bp, vehicle_spawn_point)

    def get_spawn_point(self, spawn_points):
        vehicle_spawn_point = random.choice(spawn_points)

        print("vehicle spawn point", vehicle_spawn_point)
        return vehicle_spawn_point
