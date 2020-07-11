#!/usr/bin/python

# Extract images from a bag file.

# Start up ROS pieces.
PKG = 'demo'
import roslib; roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Reading bag filename from command line or roslaunch parameter.
import os
import sys

class ImageCreator():

    index_in_filename = True
    index_format = "06d"
    image_index = 0
    encoding = "bgr8"

    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get parameters as arguments to 'rosrun my_package bag_to_images.py <save_dir> <filename> <desired_topic> <include_timestamp> <image_type>', where save_dir and filename exist relative to this executable file.
        save_dir = os.path.join(sys.path[0], sys.argv[1])
        filename = os.path.join(sys.path[0], sys.argv[2])
        desired_topic = sys.argv[3]
        include_timestamp = int(sys.argv[4])
        image_type = "." + sys.argv[5]
        rospy.loginfo("Bag filename = %s", filename)
        rospy.loginfo("Output = %s", save_dir)

        # Use a CvBridge to convert ROS images to OpenCV images so they can be saved.
        self.bridge = CvBridge()

        # Open bag file.
        with rosbag.Bag(filename, 'r') as bag:
            for topic, msg, t in bag.read_messages():
                topic_parts = topic.split('/')[1:]
                # first part is empty string
                if topic == desired_topic:
                    try:
                        if "compressed" in topic:
                            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg)
                        else:
                            cv_image = self.bridge.imgmsg_to_cv2(msg, self.encoding)
                    except CvBridgeError, e:
                        print e
                    timestr = "%.3f" % msg.header.stamp.to_sec()
                    prefix = str(save_dir) + "/"
                    # prefix = str(save_dir) + "/" + "-".join(topic_parts)
                    if include_timestamp:
                        suffix = "-" + timestr + image_type
                    else:
                        suffix = image_type
                    if self.index_in_filename:
                        image_name = prefix + format(self.image_index, self.index_format) + suffix
                    else:
                        image_name = prefix + suffix
                    rospy.loginfo(image_name)
                    cv2.imwrite(image_name, cv_image)
                    self.image_index = self.image_index + 1

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node(PKG)
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException: pass

