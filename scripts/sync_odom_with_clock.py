#!/usr/bin/python
PKG = 'demo'
import roslib; roslib.load_manifest(PKG)
import rosbag
import rospy
import message_filters
from nav_msgs.msg import Odometry

# Reading bag filename from command line or roslaunch parameter.
import os
import sys

rospy.init_node('sync_odom_with_clock')

if len(sys.argv) < 3:
    print("usage: sync_odom_with_clock.py filename_out topic")
    exit(1)
filename_out = os.path.join(sys.path[0], sys.argv[1])
topic = sys.argv[2]
rospy.loginfo("filename_out  : %s", filename_out)
rospy.loginfo("topic : %s", topic)

outbag = rosbag.Bag(filename_out, 'w')

def callback(clk_msg, odom_msg):
    odom_msg.header.stamp = clk_msg.header.stamp
    outbag.write(topic, odom_msg, clk_msg.header.stamp)
    
queue_size = 1000 # because of 200 Hz Vicon
slop = 1.
msg_clock_sub = message_filters.Subscriber("/stamp", Odometry, queue_size = 1000)

msg_odom_sub = message_filters.Subscriber(topic, Odometry, queue_size = 1000)
ts = message_filters.ApproximateTimeSynchronizer([msg_clock_sub, msg_odom_sub], queue_size, slop)
ts.registerCallback(callback)

rospy.loginfo("Start spining")
rospy.spin()
outbag.close()
exit(0)