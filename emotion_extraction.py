#!/usr/bin/env python
import cv2

import numpy
import rospy
import sys
import serial
from sensor_msgs.msg import Image
from rospy.numpy_msg import numpy_msg
from cv_bridge import CvBridge, CvBridgeError
import time

def callback_faces(data):
    frame = CvBridge().imgmsg_to_cv2(data)
    #encoding is correct - CHECKED
    cv2.imshow('Detected faces', frame)
    #imshow works only if waitKey is used after it\
    #otherwise it won't show the image

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting")

def main():
    rospy.init_node('emotion_extraction')
    rospy.Subscriber("/faces", Image , callback_faces)
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str
        rospy.spin()

if __name__ == '__main__':
    try:
        print("Just started")
        main()
    except rospy.ROSInterruptException:
        pass