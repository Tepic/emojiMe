;; Auto-generated. Do not edit!


(when (boundp 'messages::ImageArray)
  (if (not (find-package "MESSAGES"))
    (make-package "MESSAGES"))
  (shadow 'ImageArray (find-package "MESSAGES")))
(unless (find-package "MESSAGES::IMAGEARRAY")
  (make-package "MESSAGES::IMAGEARRAY"))

(in-package "ROS")
;;//! \htmlinclude ImageArray.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass messages::ImageArray
  :super ros::object
  :slots (_ImageArray ))

(defmethod messages::ImageArray
  (:init
   (&key
    ((:ImageArray __ImageArray) (let (r) (dotimes (i 0) (push (instance sensor_msgs::Image :init) r)) r))
    )
   (send-super :init)
   (setq _ImageArray __ImageArray)
   self)
  (:ImageArray
   (&rest __ImageArray)
   (if (keywordp (car __ImageArray))
       (send* _ImageArray __ImageArray)
     (progn
       (if __ImageArray (setq _ImageArray (car __ImageArray)))
       _ImageArray)))
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image[] _ImageArray
    (apply #'+ (send-all _ImageArray :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image[] _ImageArray
     (write-long (length _ImageArray) s)
     (dolist (elem _ImageArray)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image[] _ImageArray
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _ImageArray (let (r) (dotimes (i n) (push (instance sensor_msgs::Image :init) r)) r))
     (dolist (elem- _ImageArray)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get messages::ImageArray :md5sum-) "dad93653879502e47043038885f31507")
(setf (get messages::ImageArray :datatype-) "messages/ImageArray")
(setf (get messages::ImageArray :definition-)
      "sensor_msgs/Image[] ImageArray
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :messages/ImageArray "dad93653879502e47043038885f31507")


