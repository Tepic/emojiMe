
(cl:in-package :asdf)

(defsystem "emojime-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ImageArray" :depends-on ("_package_ImageArray"))
    (:file "_package_ImageArray" :depends-on ("_package"))
  ))