#!/usr/bin/python

# Rewrite periodic timestamps in a bag

# Start up ROS pieces.
PKG = 'demo'
import roslib; roslib.load_manifest(PKG)
import rosbag
import rospy

# Reading bag filename from command line or roslaunch parameter.
import os
import sys

class RewriteTimestamps():


    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get parameters as arguments to:
        # rosrun my_package rewrite_timestamp.py <filename_in> <filename_out> <copy_non_desired_topic> <desired_topic condition> <timestamp_s_start>
        #                                        <timestamp_ns_start> <timestamp_s_delta> <timestamp_ns_delta> <desired_topic condition> <timestamp_s_start> ...
        # e.g. ""
        filename_in = os.path.join(sys.path[0], sys.argv[1])
        filename_out = os.path.join(sys.path[0], sys.argv[2])
        copy_non_desired_topic = int(sys.argv[3])
        idx = 4
        desired_topics, timestamps_s_start, timestamps_ns_start, timestamps_s_delta, timestamps_ns_delta = [], [], [], [], []
        while True:
            try:
                desired_topics.append(sys.argv[idx])
                idx += 1
                timestamps_s_start.append(int(sys.argv[idx]))
                idx += 1
                timestamps_ns_start.append(int(sys.argv[idx]))
                idx += 1
                timestamps_s_delta.append(int(sys.argv[idx]))
                idx += 1
                timestamps_ns_delta.append(int(sys.argv[idx]))
                idx += 1
            except:
                print()
                break
            
        rospy.loginfo("Input  : %s", filename_in)
        rospy.loginfo("Output : %s", filename_out)
        rospy.loginfo("Copy non-desired topics : %s", copy_non_desired_topic)
        rospy.loginfo("Desired topics : %s", desired_topics)

        # Open bag file.
        desired_topic_timestamps = {}
        with rosbag.Bag(filename_out, 'w') as outbag:
            for topic, msg, t in rosbag.Bag(filename_in).read_messages():
                topic_in_desired_topics = False
                # Process every desired topic
                for desired_topic, timestamp_s_start, timestamp_ns_start, timestamp_s_delta, timestamp_ns_delta in \
                    zip(desired_topics, timestamps_s_start, timestamps_ns_start, timestamps_s_delta, timestamps_ns_delta):
                    if eval(desired_topic):
                        topic_in_desired_topics = True
                        if topic not in desired_topic_timestamps.keys(): # init
                            desired_topic_timestamps[topic] = [rospy.Time(timestamp_s_start, timestamp_ns_start)]
                        else: # extend
                            desired_topic_timestamps[topic].append(desired_topic_timestamps[topic][-1] + rospy.Duration(timestamp_s_delta, timestamp_ns_delta))
                        msg.header.stamp = desired_topic_timestamps[topic][-1]
                        outbag.write(topic, msg, msg.header.stamp)
                if copy_non_desired_topic and not topic_in_desired_topics: # Write out a non-handled message
                    outbag.write(topic, msg, msg.header.stamp)

if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node(PKG)
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        image_creator = RewriteTimestamps()
    except rospy.ROSInterruptException: pass

