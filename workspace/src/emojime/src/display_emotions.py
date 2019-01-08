#!/usr/bin/env python
import numpy
import rospy
import sys
import serial
import time

# import messages
from std_msgs.msg import Int16MultiArray

#detected_faces_previously = 0

def callback_emotions(emotions):
    data = list(emotions.data)
    detected_faces = data[0]
    emotions = data[1:]
    print detected_faces
    print emotions

def main():
    rospy.init_node('display_emotions')
    rospy.Subscriber("/emotions", Int16MultiArray , callback_emotions)
    while not rospy.is_shutdown():
        rospy.spin()
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        print("Just started")
        main()
    except rospy.ROSInterruptException:
        pass