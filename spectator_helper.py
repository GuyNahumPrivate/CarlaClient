from carla_world_facade import connect_world, clear
from carla import Location, Rotation, Transform

world = connect_world()
spectator = world.get_spectator()


def set_spectator_wide_view():
    spectator.set_transform(Transform(Location(x=19.715557, y=43.560440, z=227.136017),
                                      Rotation(pitch=-88.999451, yaw=-89.045952, roll=0.001076)))


# print(spectator.get_transform())
clear(world)
set_spectator_wide_view()
