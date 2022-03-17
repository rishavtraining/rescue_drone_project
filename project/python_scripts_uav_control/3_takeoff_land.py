'''
* Project Name: Unmanned Aerial System for flood disaster emergency response 
                and rescue management

* Author List: Krishna Nimbalkar

* Filename: 3_takeoff_land.py

* Functions: arm_and_takeoff()

* Global Variables: ConnectionString,BaudRate

'''

'''
This is a simple Python script that connects to APM over Serial port of
Raspberry Pi and then Takes off dronr to given Altitude (Relative to Ground)
Hovers there for a while and lands
'''

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

ConnectionString = "/dev/ttyS0"

BaudRate = 115200


# Connect to the Vehicle
print("Connecting to vehicle on :  ", ConnectionString)
print("Baudrate   :  "  , BaudRate)

vehicle = connect(ConnectionString, baud=BaudRate, wait_ready=True)
print("Connected to the vehicle")

# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):

  #commented for debugging
  #print( "Basic pre-arm checks")
  # Don't let the user try to arm until autopilot is ready
  #while not vehicle.is_armable:
    #print( " Waiting for vehicle to initialise...")
    #time.sleep(1)

  print("Arming motors")
  # Copter should arm in GUIDED mode
  vehicle.mode    = VehicleMode("GUIDED")
  vehicle.armed   = True

  while not vehicle.armed:
    print( " Waiting for arming...")
    time.sleep(1)

  print( "Taking off!")
  time.sleep(5)
  vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

  # Check that vehicle has reached takeoff altitude
  while True:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    #Break and return from function just below target altitude.
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
      print("Reached target altitude")
      break
    time.sleep(1)

#nitialize the takeoff sequence to 1m
arm_and_takeoff(1)

print("Take off complete")

#Hover for 10 seconds
time.sleep(10)

print("Now let's land")
vehicle.mode = VehicleMode("LAND")

# Close vehicle object
vehicle.close()
