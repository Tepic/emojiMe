#!/usr/bin/env python

# Proof-of-concept
import cv2
import sys
from constants import *
from emotion_recognition import EmotionRecognition
import numpy as np

import rospy
import serial
from sensor_msgs.msg import Image
from rospy.numpy_msg import numpy_msg
from cv_bridge import CvBridge, CvBridgeError
import time

# import messages
from messages.msg import ImageArray
from std_msgs.msg import Int16MultiArray

def format_image(image):
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # Chop image to face

    # Resize image to network size
    try:
        image = cv2.resize(image, (SIZE_FACE, SIZE_FACE),
                           interpolation=cv2.INTER_CUBIC) / 255.
    except Exception:
        print("[+] Problem during resize")
        return None
    return image

# ========================================================================
# ROS
emotion_publisher=rospy.Publisher('emotions',Int16MultiArray,queue_size = 1)

def callback_faces(data):
    global network
    global feelings_faces
    global font

    global emotion_publisher

    # Capture frame-by-frame
    emotion_Array = []
    emotion_Array += [len(data.ImageArray)]
    elements = range(len(data.ImageArray))
    for counter in elements:
        face = data.ImageArray[counter] # <-- change to display all faces ! ! !
        frame = CvBridge().imgmsg_to_cv2(face)
        # Predict result with network
        result = network.predict(format_image(frame))

        # Draw face in frame
        # for (x,y,w,h) in faces:
        #   cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Write results in frame
        if result is not None:
            face_image = feelings_faces[np.argmax(result[0])]
            emotion_Array+=[np.argmax(result[0])]

        #encoding is correct - CHECKED
        #detected_faces_previously = detected_faces_previously+1
        cv2.imshow('Detected face '+str(counter+1)+': '+face_image, frame)
        #imshow works only if waitKey is used after it\
        #otherwise it won't show the image

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting")

    msg = Int16MultiArray()
    msg.data = emotion_Array
    emotion_publisher.publish(msg)

# ========================================================================
# Load Model
network = EmotionRecognition()
network.build_network()

font = cv2.FONT_HERSHEY_SIMPLEX

feelings_faces = []
for index, emotion in enumerate(EMOTIONS):
    #feelings_faces.append(cv2.imread('./emojis/' + emotion + '.png', -1))
    feelings_faces += [emotion]

def main():
    rospy.init_node('emotion_extraction')
    rospy.Subscriber("/faces", ImageArray , callback_faces)

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str
        rospy.spin()
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        print("Just started")
        main()
    except rospy.ROSInterruptException:
        pass