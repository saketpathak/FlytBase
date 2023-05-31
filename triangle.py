#Triangle of side length 10m

#!/user/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)

time.sleep(3)

print 'taking off at 10m altitude'
drone.take_off(10.0)

print ' Starts to make a triangle of side length 10m'

print ' 1st waypoint'
drone.position_set(8.66,5.0,0,relative=True)

print ' 2nd waypoint'
drone.position_set(-8.66,5.0,0,relative=True)

print ' 3rd waypoint'
drone.position_set(0,-10.0,0,relative=True)

print 'Landing after completing all the waypoints'
drone.land(async=False)

drone.disconnect()

