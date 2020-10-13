#! /usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
print "d1keyboard_input"




rospy.init_node('d1keyboard_input')
pub = rospy.Publisher('/key_press', String, queue_size=1)

while(True):

    val = raw_input("Input W/A/S/D: ")
    #print("hello, " + val)
    pub.publish(val)

rospy.spin()