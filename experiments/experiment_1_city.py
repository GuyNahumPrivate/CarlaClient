from carla import Location, Rotation
from preference_factors_config import prefer_city_factors
from Main import run_script
import carla

run_script(road_type_factors=prefer_city_factors,
           target_speed=40,
           opt_dict={'ignore_traffic_lights': True, 'ignore_stop_signs': True},
           destination=Location(x=-41.825058, y=-19.16032, z=0.600000),
           spawn_point=carla.Transform(Location(x=99.396645, y=-4.497115, z=0.600000),
                              Rotation(pitch=360.000000, yaw=-269.609222, roll=0.000000)),
           debug=False)

