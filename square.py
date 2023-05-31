#Square of side length 6.5m

#!/user/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)

time.sleep(3)

print "taking off and hover at 5m altitude"
drone.take_off(5.0)

print " Starts to make a square of side length 6.5m"

print " 1st waypoint"
drone.position_set(6.5,0,0,relative=True)
print " 2nd waypoint"
drone.position_set(0,6.5,0,relative=True)
print " 3rd waypoint"
drone.position_set(-6.5,0,0,relative=True)
print " 4th waypoint"
drone.position_set(0,-6.5,0,relative=True)

print " Landing after completing all the waypoints"
drone.land(async=False)

drone.disconnect()


