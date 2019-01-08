;; Auto-generated. Do not edit!


(when (boundp 'emojime::ImageArray)
  (if (not (find-package "EMOJIME"))
    (make-package "EMOJIME"))
  (shadow 'ImageArray (find-package "EMOJIME")))
(unless (find-package "EMOJIME::IMAGEARRAY")
  (make-package "EMOJIME::IMAGEARRAY"))

(in-package "ROS")
;;//! \htmlinclude ImageArray.msg.html


(defclass emojime::ImageArray
  :super ros::object
  :slots (_custom_msg ))

(defmethod emojime::ImageArray
  (:init
   (&key
    ((:custom_msg __custom_msg) "")
    )
   (send-super :init)
   (setq _custom_msg (string __custom_msg))
   self)
  (:custom_msg
   (&optional __custom_msg)
   (if __custom_msg (setq _custom_msg __custom_msg)) _custom_msg)
  (:serialization-length
   ()
   (+
    ;; string _custom_msg
    4 (length _custom_msg)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _custom_msg
       (write-long (length _custom_msg) s) (princ _custom_msg s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _custom_msg
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _custom_msg (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get emojime::ImageArray :md5sum-) "34bc0b7b6938cfa2480828862cdaf1a1")
(setf (get emojime::ImageArray :datatype-) "emojime/ImageArray")
(setf (get emojime::ImageArray :definition-)
      "string custom_msg

")



(provide :emojime/ImageArray "34bc0b7b6938cfa2480828862cdaf1a1")


