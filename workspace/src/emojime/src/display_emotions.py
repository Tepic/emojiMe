#!/usr/bin/env python
import numpy
import rospy
import sys
import serial
import time
import numpy as np

# import messages
from std_msgs.msg import Int16MultiArray

#detected_faces_previously = 0

def callback_emotions(emotions):
    data = list(emotions.data)
    detected_faces = data[0]
    emotions = data[1:]
    print detected_faces
    print emotions

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

    anngry = angry+disguisted+fearful

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