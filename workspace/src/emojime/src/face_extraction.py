#!/usr/bin/env python
import face_recognition
import cv2

import numpy
import rospy
import sys
import serial
from sensor_msgs.msg import Image
from rospy.numpy_msg import numpy_msg
from cv_bridge import CvBridge, CvBridgeError
import time

# import messages
from messages.msg import ImageArray

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

process_this_frame = 1
processing_in_progress = 0
face_publisher=rospy.Publisher('faces',ImageArray,queue_size = 1)
message_imageArray = ImageArray()

def extract_faces(frame):
    global message_imageArray
    global process_this_frame
    global face_publisher

    #message_imageArray.ImageArray = frame

    # Only process every other frame of video to save time
    if process_this_frame%(25*1)==0:
        process_this_frame = 1 

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Publish the results
        to_publish = 0
        message_imageArray.ImageArray = []
        for (top, right, bottom, left) in face_locations:
            face_frames = frame
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            #cv2.rectangle(face_frames, (left, top), (right, bottom), (0, 0, 255), 2)

            # Crop image
            face_frames = face_frames[top:bottom,left:right]

            # print(face_frames.shape) # Output: (480, 640, 3)
            msg_frame = CvBridge().cv2_to_imgmsg(face_frames, encoding="passthrough")
            message_imageArray.ImageArray.append(msg_frame)
            to_publish = 1
        if to_publish==1:
            face_publisher.publish(message_imageArray)

    process_this_frame = process_this_frame+1

def callback_live_video(data):    
    global processing_in_progress
    frame = CvBridge().imgmsg_to_cv2(data)
    if(processing_in_progress==0):
        processing_in_progress = 1
        #print('Finding faces')
        extract_faces(frame)
        #print('Faces found')
        processing_in_progress = 0

def main():
    global face_publisher
    rospy.init_node('face_extraction')
    face_publisher=rospy.Publisher('faces',ImageArray,queue_size = 1)
    rospy.Subscriber("/live_video", Image , callback_live_video)

    while not rospy.is_shutdown():
        print('Waiting')
        rospy.spin()

if __name__ == '__main__':
    try:
        print("Just started")
        main()
    except rospy.ROSInterruptException:
        pass