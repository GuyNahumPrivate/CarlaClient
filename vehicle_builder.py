import carla
import random


class VehicleBuilder:
    vehicle_model = 'vehicle.lincoln.mkz_2020'

    def a_vehicle(self, world: carla.World):
        map = world.get_map()
        bp_lib = world.get_blueprint_library()
        spawn_points = map.get_spawn_points()
        vehicle_bp = bp_lib.find(self.vehicle_model)
        self.vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

        return world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))