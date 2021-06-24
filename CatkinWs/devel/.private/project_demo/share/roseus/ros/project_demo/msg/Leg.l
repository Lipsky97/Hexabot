;; Auto-generated. Do not edit!


(when (boundp 'project_demo::Leg)
  (if (not (find-package "PROJECT_DEMO"))
    (make-package "PROJECT_DEMO"))
  (shadow 'Leg (find-package "PROJECT_DEMO")))
(unless (find-package "PROJECT_DEMO::LEG")
  (make-package "PROJECT_DEMO::LEG"))

(in-package "ROS")
;;//! \htmlinclude Leg.msg.html


(defclass project_demo::Leg
  :super ros::object
  :slots (_tigh _knee _foot ))

(defmethod project_demo::Leg
  (:init
   (&key
    ((:tigh __tigh) 0.0)
    ((:knee __knee) 0.0)
    ((:foot __foot) 0.0)
    )
   (send-super :init)
   (setq _tigh (float __tigh))
   (setq _knee (float __knee))
   (setq _foot (float __foot))
   self)
  (:tigh
   (&optional __tigh)
   (if __tigh (setq _tigh __tigh)) _tigh)
  (:knee
   (&optional __knee)
   (if __knee (setq _knee __knee)) _knee)
  (:foot
   (&optional __foot)
   (if __foot (setq _foot __foot)) _foot)
  (:serialization-length
   ()
   (+
    ;; float32 _tigh
    4
    ;; float32 _knee
    4
    ;; float32 _foot
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _tigh
       (sys::poke _tigh (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _knee
       (sys::poke _knee (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _foot
       (sys::poke _foot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _tigh
     (setq _tigh (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _knee
     (setq _knee (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _foot
     (setq _foot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get project_demo::Leg :md5sum-) "5da4b1c2eb62b548b44603075da2f338")
(setf (get project_demo::Leg :datatype-) "project_demo/Leg")
(setf (get project_demo::Leg :definition-)
      "#tigh
float32 tigh
#knee
float32 knee
#foot
float32 foot

")



(provide :project_demo/Leg "5da4b1c2eb62b548b44603075da2f338")


