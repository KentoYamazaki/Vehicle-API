from kuksa_client.grpc import VSSClient

with VSSClient('127.0.0.1', 55555) as client:
    
    # Subscribe 'Vehicle.Body.Trunk.Rear.IsOpen'
    for updates in client.subscribe_target_values([
        'Vehicle.Body.Trunk.Rear.IsOpen',
    ]):
        # Check the request content.(Open(True) or close(False))
        request_trunk_status = updates['Vehicle.Body.Trunk.Rear.IsOpen'].value
        print(f"[trunk_door_service_provider] Received updated Vehicle.Body.Trunk.Rear.IsOpen': {request_trunk_status}")
        if request_trunk_status:
            print(f"[trunk_door_service_provider] Closed the door !")
        else:
            print(f"[trunk_door_service_provider] Opened the door !")
