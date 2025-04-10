#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber():
    def __init__(self):
        self.sub = rospy.Subscriber(
            '/usb_cam/image_raw',
            Image,
            self.listener_callback,
            queue_size=10)
        self.br = CvBridge()
    
    def listener_callback(self, msg):
        current_frame = self.br.imgmsg_to_cv2(msg)
        rgb_image = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR) ## ROS is RGB, OpenCV is BGR
        cv2.imshow("Original", rgb_image)
        cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node("image_viewer", anonymous=True)
    image_subscriber = ImageSubscriber()
    rospy.spin()

