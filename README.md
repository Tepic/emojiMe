# emojiMe

## Sources:

[1] Face Recognition:
https://github.com/ageitgey/face_recognition

[2] Emotion Recognition:
https://github.com/isseu/emotion-recognition-neural-networks

## Installation:

### Step 1 - ROS
Recommended to use Ubuntu 18.04 since this code was developed tested and ran on this OS.

_Currently testing_: Ubuntu 16.04

|         OS       |  ROS version  | Instalation Reference [link] |
|------------------|---------------|------------------------------|
|   Ubuntu 18.04   |    Melodic    |http://wiki.ros.org/melodic/Installation/Ubuntu|
|   Ubuntu 16.04   |    Kinetic    |http://wiki.ros.org/kinetic/Installation/Ubuntu|

```
# Melodic installation [FULL]

$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
$ sudo apt update

$ sudo apt install ros-melodic-desktop-full

$ apt search ros-melodic

$ sudo rosdep init
$ rosdep update

$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
# check in ~/.bashrc file if the copied command source /..../setup.bash is copied in right way at the end of ~/.bashrc file
# since if something was already sourced to this file, the executed command will just appends the path
# to the last line in file instead to add it in the new  (separate) line

# now source it
$ source ~/.bashrc

# and finally ROS-python dependencies
$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```
### Step 2 - Face recognition
In this work we have used python(2) version. In reference [1] they have used pip3, but we will use just a pip for executing the following command to install face_recognition library for python:

```
$ pip3 install face_recognition
```
According to [1]: If you are having trouble with installation, you can also try out a [pre-configured VM](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b).

### Step 3 - Clone this repo
Now clone this repo. It is already prepaired for using with ROS - meaning workspace is already created.

Navigate to ../emojiMe/workspace/src/emojime/src/Code/emotion-recognition-neural-networks-master/

Execute:
```
$ sudo apt-get install python-pip python-dev python-virtualenv
```

Furthermore, execute the following commands to install further dependencies -> go to Step 4 - Emotion recognition

### Step 4 - Emotion recognition [2]
```
# in original repo they used python3
# $ virtualenv -p python3 ./
$ virtualenv -p python ./

$ source ./bin/activate
$ pip install -r requirements.txt
```
## Run it
Finally, compile the code:
```
$ cd ~/../emojiMe/workspace/
$ catkin_make
```

Now, in order to use the code open 5 terminalsL
**Terminal 1**
Start ROS
```
# Terminal 1
$ roscore
```
**Terminal 2**
Start camera. There are two cameras - webCAM (USB cam) and IP CAM.
How to install IP CAM [here](https://thecodacus.com/ip-webcam-opencv-wireless-camera/)
```
# Terminal 2
$ cd ~/../emojiMe/workspace/src/emojime/src/
$ python live_video.py
```
**Terminal 3**
Start algorithm to extract faces
```
# Terminal 3
$ cd ~/../emojiMe/workspace/
$ source devel/setup.bash
$ roslaunch emojime launch_face_extraction.launch
```
**Terminal 4**
Start algorithm to extract emotions from images received as ImageVector over ROS pub/sub. This message is custom made.
```
# Terminal 4
$ cd ~/../emojiMe/workspace/
$ source devel/setup.bash
$ roslaunch emojime launch_show_emotions.launch 
# $ roslaunch emojime launch_emotion_extraction.launch
```
**Terminal 5**
Start algorithm to extract emotions from images received as ImageVector over ROS pub/sub. This message is custom made.
```
# Terminal 5
$ cd ~/../emojiMe/workspace/
$ python display_emotions.py
```

Communication of system looks like (for now):

![alt text](/emojiME_ROS_msgs.jpeg)

=================================================================

### Disregard the rest (internal stuff/notes)

rostensorflow

- Install TensorFlow (see [tensor flow install guide](https://www.tensorflow.org/install/install_linux))
- Install ROS (see http://wiki.ros.org)
- Install cv-bridge

```bash
$ sudo apt-get install ros-kinetic-cv-bridge ros-kinetic-opencv3
```

- (Optional) Install camera driver (for example, cv_camera)

```bash
$ sudo apt-get install ros-kinetic-cv-camera
```

TensorFlow install note (without GPU)
-------------------------------------------
Please read official guide. This is a only note for me.

```bash
$ sudo apt-get install python-pip python-dev python-virtualenv
$ virtualenv --system-site-packages ~/tensorflow
$ source ~/tensorflow/bin/activate
$ pip install --upgrade tensorflow
```

image_recognition.py
--------------------------------

* publish: /result (std_msgs/String)
* subscribe: /image (sensor_msgs/Image)

How to try

```bash
$ roscore
$ rosrun cv_camera cv_camera_node
$ source ~/tensorflow/bin/activate
$ python image_recognition.py image:=/cv_camera/image_raw
$ rostopic echo /result
```
