#!/usr/bin/env python
import numpy
import rospy
import sys
import serial
import time
import numpy as np
import showResults

# threading
import threading
import time
import sys

# import messages
from std_msgs.msg import Int16MultiArray

#detected_faces_previously = 0

global satisfied_input
global shocked_input
global neutral_input
global bored_input

satisfied_input = 0
shocked_input   = 0
neutral_input   = 0
bored_input     = 0

global counter
counter = 0

global __DEBUG__
__DEBUG__ = False

def callback_emotions(emotions):
    global counter
    global __DEBUG__

    data = list(emotions.data)
    detected_faces = data[0]
    emotions = data[1:]
    #print detected_faces
    #print emotions

    # check these things out
    print('Emotions')
    angry = emotions.count(0)
    #print angry
    disguisted  = emotions.count(1)
    #print disguisted
    fearful = emotions.count(2)
    #print fearful
    happy = emotions.count(3)
    #print happy
    sad = emotions.count(4)
    #print sad
    surprised = emotions.count(5)
    #print surprised
    neutral = emotions.count(6)
    #print neutral

    angry = angry+disguisted+fearful

    emoticons_percentage = []
    emoticons_percentage.append(angry)
    emoticons_percentage.append(happy)
    emoticons_percentage.append(sad)
    emoticons_percentage.append(surprised)
    emoticons_percentage.append(neutral)
    emoticons_percentage = (100.0/detected_faces)*np.array(emoticons_percentage)
    #print emoticons_percentage
    #print('Angry\tDisguisted\tFearful\tHappy\tSad\tSurprised\tNeutral')
    #print('======================================================================')
    #print(str(emoticons_percentage[0])+'\t\t'+str(emoticons_percentage[1])+'\t'+str(emoticons_percentage[2])+'\t'+str(emoticons_percentage[3])+'\t'+str(emoticons_percentage[4])+'\t'+str(emoticons_percentage[5])+'\t\t'+str(emoticons_percentage[6]))

    print('Angry\tHappy\tSad\tSurprised\tNeutral')
    print('======================================================================')
    print(str(emoticons_percentage[0])+'\t'+str(emoticons_percentage[1])+'\t'+str(emoticons_percentage[2])+'\t'+str(emoticons_percentage[3])+'\t\t'+str(emoticons_percentage[4]))

    satisfied_input = emoticons_percentage[1]
    shocked_input   = emoticons_percentage[0]+emoticons_percentage[3]
    neutral_input   = emoticons_percentage[4]
    bored_input     = emoticons_percentage[2]

    if(__DEBUG__):
        counter = counter+1
        print("counter: %i" % counter)

    if(__DEBUG__):
        print("Update results")
    showResults.setNewResults(satisfied_input,shocked_input,neutral_input,bored_input)
    new_data_available = False

def display():
    while(True):
        print("executing")
        showResults.main()

def main():
    global new_data_available

    rospy.init_node('display_emotions')
    rospy.Subscriber("/emotions", Int16MultiArray , callback_emotions)
    while not rospy.is_shutdown():        
        rospy.spin()
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:        
        display_thread = threading.Thread(target=display)
        display_thread.daemon = True

        print("Just started")
        display_thread.start()
        
        main()
        
    except rospy.ROSInterruptException:
        pass