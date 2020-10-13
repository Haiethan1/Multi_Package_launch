#! /usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import String

print "d1move_robot"


tt0 = None
def callback(msg):
    print msg.data
    d = msg.data 
    tw = Twist()
    if (d == "w"):
        tw.linear.x = 0.5
    elif (d == "s"):
        tw.linear.x = -0.5
    elif ( d == "d"):
        tw.angular.z = -0.5
    elif (d == "a"):
        tw.angular.z = 0.5
    else:
        pass
    pub.publish(tw)

rospy.init_node('d1move_robot')
sub = rospy.Subscriber('/key_press', String, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
