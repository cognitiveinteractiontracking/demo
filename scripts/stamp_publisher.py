#!/usr/bin/python
PKG = 'demo'
import roslib
roslib.load_manifest(PKG)
import rospy, sys, os
 
#remove or add the message type
from nav_msgs.msg import Odometry

rospy.init_node('stamp_publisher')

pub=rospy.Publisher('/stamp', Odometry, queue_size=1, latch=False)

if len(sys.argv) < 2:
    print("usage: stamp_publisher.py rate")
    exit(1)
rate = float(sys.argv[1])
rospy.loginfo("rate : %f", rate)

#set a publishing rate. Below is a publishing rate of 10 times/second
r=rospy.Rate(rate)

msg = Odometry()

while not rospy.is_shutdown():
    msg.header.stamp = rospy.get_rostime()
    pub.publish(msg)
    r.sleep()
    
    