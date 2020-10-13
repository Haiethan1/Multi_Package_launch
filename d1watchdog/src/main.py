#! /usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
import time as t
from std_msgs.msg import String

print "d1watchdog"

MAX_TIME = 2.0

# starting tiem
t0 = t.time()

def callback(msg):
    global t0
    t0 = t.time()
    print msg.data

        

rospy.init_node('d1move_robot')
sub = rospy.Subscriber('/key_press', String, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

while(True):
    t1 = t.time()
    dt = t1 - t0
    if (dt > MAX_TIME):
        tw = Twist()
        pub.publish(tw)
        #print "timeout"
    t.sleep(0.1)