
(cl:in-package :asdf)

(defsystem "project_demo-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Leg" :depends-on ("_package_Leg"))
    (:file "_package_Leg" :depends-on ("_package"))
  ))