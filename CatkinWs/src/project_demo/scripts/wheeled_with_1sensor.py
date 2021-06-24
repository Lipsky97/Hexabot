#! /usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Twist, PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Bool, Float32

rospy.init_node("demo")

triggered = False

def sensorTrigger(msg):
    global triggered
    triggered = msg.data

    if triggered==True:
        rospy.loginfo("I see something")

def drive_forward():
    rospy.loginfo("driving")
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = -1
    publ.publish(msg)
    pubr.publish(msg)

def turn_left():
    rospy.loginfo("turning left")
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = 1
    publ.publish(msg)

def turn_right():
    rospy.loginfo("turning right")
    pubr = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = 1
    pubr.publish(msg)

def full_stop():
    rospy.loginfo("Full stop")
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = 0
    publ.publish(msg)
    pubr.publish(msg)



if __name__ == '__main__':

    rospy.Subscriber('/sensorTrigger', Bool, sensorTrigger)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)

    full_stop()
    drive_forward()

    r = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        if triggered == False:
            drive_forward()
        elif triggered == True:
            while triggered == True:
                turn_right()
            full_stop()
            drive_forward()
        r.sleep()
    rospy.spin()