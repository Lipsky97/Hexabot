; Auto-generated. Do not edit!


(cl:in-package project_demo-msg)


;//! \htmlinclude Leg.msg.html

(cl:defclass <Leg> (roslisp-msg-protocol:ros-message)
  ((tigh
    :reader tigh
    :initarg :tigh
    :type cl:float
    :initform 0.0)
   (knee
    :reader knee
    :initarg :knee
    :type cl:float
    :initform 0.0)
   (foot
    :reader foot
    :initarg :foot
    :type cl:float
    :initform 0.0))
)

(cl:defclass Leg (<Leg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Leg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Leg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name project_demo-msg:<Leg> is deprecated: use project_demo-msg:Leg instead.")))

(cl:ensure-generic-function 'tigh-val :lambda-list '(m))
(cl:defmethod tigh-val ((m <Leg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_demo-msg:tigh-val is deprecated.  Use project_demo-msg:tigh instead.")
  (tigh m))

(cl:ensure-generic-function 'knee-val :lambda-list '(m))
(cl:defmethod knee-val ((m <Leg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_demo-msg:knee-val is deprecated.  Use project_demo-msg:knee instead.")
  (knee m))

(cl:ensure-generic-function 'foot-val :lambda-list '(m))
(cl:defmethod foot-val ((m <Leg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader project_demo-msg:foot-val is deprecated.  Use project_demo-msg:foot instead.")
  (foot m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Leg>) ostream)
  "Serializes a message object of type '<Leg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'tigh))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'knee))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'foot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Leg>) istream)
  "Deserializes a message object of type '<Leg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tigh) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'knee) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'foot) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Leg>)))
  "Returns string type for a message object of type '<Leg>"
  "project_demo/Leg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Leg)))
  "Returns string type for a message object of type 'Leg"
  "project_demo/Leg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Leg>)))
  "Returns md5sum for a message object of type '<Leg>"
  "5da4b1c2eb62b548b44603075da2f338")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Leg)))
  "Returns md5sum for a message object of type 'Leg"
  "5da4b1c2eb62b548b44603075da2f338")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Leg>)))
  "Returns full string definition for message of type '<Leg>"
  (cl:format cl:nil "#tigh~%float32 tigh~%#knee~%float32 knee~%#foot~%float32 foot~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Leg)))
  "Returns full string definition for message of type 'Leg"
  (cl:format cl:nil "#tigh~%float32 tigh~%#knee~%float32 knee~%#foot~%float32 foot~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Leg>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Leg>))
  "Converts a ROS message object to a list"
  (cl:list 'Leg
    (cl:cons ':tigh (tigh msg))
    (cl:cons ':knee (knee msg))
    (cl:cons ':foot (foot msg))
))
