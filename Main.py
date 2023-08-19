import carla
from MyVehicle import MyVehicle

serverIP = 'localhost'
serverPort = 2000

client = carla.Client(serverIP, serverPort)
world = client.get_world()
bp_lib = world.get_blueprint_library()

vehicle = MyVehicle(world)

