# emojiMe

Create packages acc. Nuclino

```
# Terminal 1
$ roscore

# Terminal 2
$ cd ~/Documents/Cloud/NextCloud/_M21/Multimodal\ Interaction\ for\ Ubiquitous\ Computers/\[06\]\ Git-Codes/emojiMe/workspace/src/emojime/src
$ python live_video.py

# Terminal 3 & 4
$ cd ~/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace
$ source devel/setu.bash 							  # repeat for both terminals
$ roslaunch emojime launch_face_extraction.launch     # terminal 2
$ roslaunch emojime launch_emotion_extraction.launch  # terminal 3
```

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
=======
>>>>>>> ccb3c4ee094d93f874049085b4a9f5cd66043202
