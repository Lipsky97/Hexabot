#! /usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Twist, PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Bool, Float32

rospy.init_node("demo")

leftTriggered = False
rightTriggered = False

def leftSensorTrigger(msg):
    global leftTriggered
    leftTriggered = msg.data

def rightSensorTrigger(msg):
    global rightTriggered
    rightTriggered = msg.data

def drive_forward():
    rospy.loginfo("driving")
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = -2
    publ.publish(msg)
    pubr.publish(msg)

def turn_left():
    r = rospy.Rate(0.5)
    while rightTriggered == True:
        rospy.loginfo("turning left")
        publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
        pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
        msg = Float32()
        msg.data = 1
        publ.publish(msg)
        msg.data = -1
        pubr.publish(msg)
        r.sleep()

def turn_right():
    r = rospy.Rate(0.5)
    while leftTriggered == True:
        rospy.loginfo("turning right")
        publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
        pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
        msg = Float32()
        msg.data = -1
        publ.publish(msg)
        msg.data = 1
        pubr.publish(msg)
        r.sleep()

def full_stop():
    rospy.loginfo("Full stop")
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    msg = Float32()
    msg.data = 0
    publ.publish(msg)
    pubr.publish(msg)



if __name__ == '__main__':

    rospy.Subscriber('/leftSensorTrigger', Bool, leftSensorTrigger)
    rospy.Subscriber('/rightSensorTrigger', Bool, rightSensorTrigger)
    pubr = rospy.Publisher('/rightMotorSpeed', Float32, queue_size=5)
    publ = rospy.Publisher('/leftMotorSpeed', Float32, queue_size=5)

    full_stop()
    drive_forward()

    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        if leftTriggered == False and rightTriggered == False:
            drive_forward()
        elif leftTriggered == True and rightTriggered == True:
            full_stop()
            turn_left()
        elif leftTriggered == True:
            full_stop()
            turn_right()
        elif leftTriggered == False and rightTriggered == True:
            full_stop()
            turn_left()
        r.sleep()
    rospy.spin()