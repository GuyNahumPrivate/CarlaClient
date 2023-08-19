import calra
import random

# carla.Vehicle
#https://carla.readthedocs.io/en/latest/python_api/#carlavehicle
class MyVehicle:
    vehicle_model = 'vehicle.lincoln.mkz_2020'

    def __init__(self, world: carla.World):
        map = world.get_map()
        bp_lib = world.get_blueprint_library()
        spawn_points = map.get_spawn_points()
        vehicle_bp = bp_lib.find(self.vehicle_model)
        self.vehicle = world.try_spawn_actor(vehicle_bp, random.choice(spawn_points))

    def setAutoPilot(self):
        self.vehicle.set_autopilot(True)

    def setManual(self):
        self.vehicle.set_autopilot(False)

    def setSpeed(self, speed):
        self.vehicle.set_target_velocity(speed)

    def stop(self):
        self.vehicle.apply_control(carla.VehicleControl(brake=1.0))

    def turnRight(self):
        control = self.vehicle.get_control()
        control.steer = 0.3
        control.throttle = 0.1
        self.vehicle.apply_control(control)

    def turnLeft(self):
        self.vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=-0.3))