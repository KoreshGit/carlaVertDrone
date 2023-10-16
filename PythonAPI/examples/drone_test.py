#!/usr/bin/env python

# Copyright (c) 2021 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Example script to generate traffic in the simulation"""

import glob
import os
import sys
import time
import numpy
from numpy import random

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
    
except IndexError:
    pass

import carla


from carla import command
from carla import Drone
from carla import Vehicle

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    # Get the blueprint library
    blueprint_library = world.get_blueprint_library()

    # Get all available blueprints
    #for ble in blueprint_library:
        #print(ble)

    blueprints = blueprint_library.filter('*lea*')
    print(random.choice(blueprints))
    spawn_point = carla.Transform(carla.Location(x=28.7, y=28.104216, z=0.690000), carla.Rotation(pitch=0.000000, yaw=0.159198, roll=0.000000))#random.choice(world.get_map().get_spawn_points())
    print(spawn_point)
    
    vehicle: Drone = world.spawn_actor(random.choice(blueprints), spawn_point)
    print(isinstance(vehicle,Drone))
    try:
        
        spectator=world.get_spectator()
        spectator.set_transform(carla.Transform(vehicle.get_location()+ carla.Location(x=-5)  + carla.Location(z=5), carla.Rotation(pitch=-40)))
        settings = world.get_settings()
        settings.synchronous_mode = True
        settings.fixed_delta_seconds = 0.03

        world.apply_settings(settings) 
        #my_comm
        # Print the names of all blueprints
        print(vehicle)
        time.sleep(3)
        while True:
            world.tick()
            
            spectator.set_transform(carla.Transform(vehicle.get_location()+ carla.Location(y=-5) + carla.Location(x=-5)  + carla.Location(z=5), carla.Rotation(pitch=-45)))
            angular_impulse = carla.Vector3D(0, 0, 20000)
            #vehicle.add_printer(angular_impulse)
            vehicle.apply_control_d()
            print(vehicle.get_location())
            #vehicle.set_terutes(True)
            #my_command=command.add_printer(vehicle,)
            #my_command=command.ApplyPrinter(vehicle,angular_impulse)
            #client.apply_batch([my_command])
            time.sleep(0.03)
       
    except Exception as e:

        print(f"An error occurred: {e}")
    finally:
        settings.synchronous_mode = False
        world.apply_settings(settings)
        vehicle.destroy()

if __name__ == '__main__':
    main()
