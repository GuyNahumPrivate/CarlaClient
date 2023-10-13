import random
import carla

class AutoDrive:
    def __init__(self, vehicle, agent, spectator, spawn_points):
        self.vehicle = vehicle
        self.agent = agent
        self.spectator = spectator
        self.spawn_points = spawn_points

    # Set the agent destination
    def set_random_destination(self):
        destination = random.choice(self.spawn_points).location
        self.agent.set_destination(destination)

    def set_spectator(self):
        transform = carla.Transform(self.vehicle.get_transform().transform(carla.Location(x=-8, z=2.5)),
                                    self.vehicle.get_transform().rotation)
        self.spectator.set_transform(transform)

    def start_game_loop(self):
        print("starting game loop")
        self.set_random_destination()

        while True:
            self.set_spectator()

            if self.agent.done():
                self.set_random_destination()
                print("The target has been reached, searching for another target")

            control = self.agent.run_step()
            self.vehicle.apply_control(control)
