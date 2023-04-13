from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

import time

with VSSClient('127.0.0.1', 55555) as client:
    for i in range(100):
        # Get VSS data
        trunk_vss_response = client.get_target_values([
            'Vehicle.Body.Trunk.Rear.IsOpen',
        ])
        # Get current trunk status
        is_trunk_open = trunk_vss_response["Vehicle.Body.Trunk.Rear.IsOpen"].value

        if(is_trunk_open):
            client.set_target_values({
                'Vehicle.Body.Trunk.Rear.IsOpen': Datapoint(False),
            })
            print(f"[client] Setting Vehicle.Body.Trunk.Rear.IsOpen to False")
            time.sleep(2)
        else:
            client.set_target_values({
                'Vehicle.Body.Trunk.Rear.IsOpen': Datapoint(True),
            })
            print(f"[client] Setting Vehicle.Body.Trunk.Rear.IsOpen to True")
            time.sleep(2)