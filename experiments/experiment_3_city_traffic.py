from carla import Location, Rotation, Transform
from preference_factors_config import prefer_city_factors
from Main import run_script


run_script(road_type_factors=prefer_city_factors,
           target_speed=20,
           opt_dict={'ignore_traffic_lights': True, 'ignore_stop_signs': True},
           destination=Location(x=-47.280842, y=13.381462, z=0.600000),
           spawn_point=Transform(Location(x=96.932175, y=7.823234, z=0.600000),
                                 Rotation(pitch=360.000000, yaw=127.679413, roll=0.000000)),
           debug=False,
           print_waypoints=False)

