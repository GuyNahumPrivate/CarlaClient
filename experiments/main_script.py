from carla import Location, Rotation, Transform
from preference_factors_config import get_road_type_factors
from Main import run_script
import carla


run_script(road_type_factors=get_road_type_factors(),
           target_speed=40,
           opt_dict={'ignore_traffic_lights': True, 'ignore_stop_signs': True},
           destination=Location(x=6.006511, y=66.283257, z=0.600000),
           spawn_point=Transform(carla.Location(x=0.445544, y=13.185217, z=0.600000),
                                 Rotation(pitch=360, yaw=-179.840790, roll=0)),
           debug=False)
