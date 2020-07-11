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

rospy.init_node('sync_odom')

if len(sys.argv) < 4:
    print("usage: sync_msg.py topic_1 topic_2 filename_out")
    exit(1)
topic_1 = sys.argv[1]
topic_2 = sys.argv[2]
filename_out = os.path.join(sys.path[0], sys.argv[3])
rospy.loginfo("topic_1  : %s", topic_1)
rospy.loginfo("topic_2  : %s", topic_2)
rospy.loginfo("filename_out  : %s", filename_out)

outbag = rosbag.Bag(filename_out, 'w')

def callback(msg_1, msg_2):
    outbag.write(topic_1, msg_1, msg_1.header.stamp)
    outbag.write(topic_2, msg_2, msg_1.header.stamp) # msg_1 stamp is on purpose for sync

msg_1_sub = message_filters.Subscriber(topic_1, Odometry, queue_size = 1000)
msg_2_sub = message_filters.Subscriber(topic_2, Odometry, queue_size = 1000)
#msg_1_sub = message_filters.Subscriber(topic_1)
#msg_2_sub = message_filters.Subscriber(topic_2)

queue_size = 1000 # because of 200 Hz Vicon
slop = 1.
ts = message_filters.ApproximateTimeSynchronizer([msg_1_sub, msg_2_sub], queue_size, slop)
ts.registerCallback(callback)
rospy.loginfo("Start spining",)
rospy.spin()
outbag.close()
exit(0)