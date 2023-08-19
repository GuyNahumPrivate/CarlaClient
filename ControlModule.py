# import carla
#
#
# class CarlaVehicleController:
#     def __init__(self, vehicle):
#         self.client = carla.Client(host, port)
#         self.client.set_timeout(10.0)
#         self.world = self.client.get_world()
#         self.vehicle = None
#
#     def spawn_vehicle(self, blueprint_name, spawn_point):
#         blueprint_library = self.world.get_blueprint_library()
#         vehicle_blueprint = blueprint_library.find(blueprint_name)
#
#         if vehicle_blueprint is None:
#             raise ValueError(f"Vehicle blueprint '{blueprint_name}' not found.")
#
#         self.vehicle = self.world.spawn_actor(vehicle_blueprint, spawn_point)
#         return self.vehicle
#
#     def control_vehicle(self, throttle, steer, brake):
#         if self.vehicle is None:
#             raise ValueError("No vehicle spawned.")
#
#         control = carla.VehicleControl()
#         control.throttle = throttle
#         control.steer = steer
#         control.brake = brake
#         control.hand_brake = False
#         control.reverse = False
#
#         self.vehicle.apply_control(control)
#
#     def destroy_vehicle(self):
#         if self.vehicle is not None:
#             self.vehicle.destroy()
#             self.vehicle = None
#
# if __name__ == "__main__":
#     host = "localhost"
#     port = 2000
#     spawn_point = carla.Transform(carla.Location(x=0, y=0, z=2), carla.Rotation(yaw=0))
#
#     controller = CarlaVehicleController(host, port)
#     controller.spawn_vehicle("vehicle.tesla.model3", spawn_point)
#
#     try:
#         while True:
#             # Example control inputs: throttle, steer, brake
#             controller.control_vehicle(throttle=0.5, steer=0.0, brake=0.0)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         controller.destroy_vehicle()