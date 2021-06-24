#! /usr/bin/env python
import rospy
import actionlib
from project_demo.msg import Leg
from std_msgs.msg import Float32, Bool

rospy.init_node("walking")

#0 frontLeft
#1 frontRight
#2 middleLeft
#3 middleRight
#4 backLeft
#5 bakcRight

pub = [rospy.Publisher('/frontLeftLeg', Leg, queue_size=5), 
rospy.Publisher('/frontRightLeg', Leg, queue_size=5),
rospy.Publisher('/middleLeftLeg', Leg, queue_size=5), 
rospy.Publisher('/middleRightLeg', Leg, queue_size=5), 
rospy.Publisher('/backLeftLeg', Leg, queue_size=5), 
rospy.Publisher('/backRightLeg', Leg, queue_size=5)]

time_now = 0.0

leftTrigger = False
rightTrigger = False

fLPos = [0, 0, 0]
fRPos = [0, 0, 0]
mLPos = [0, 0, 0]
mRPos = [0, 0, 0]
bLPos = [0, 0, 0]
bRPos = [0, 0, 0]

legTouch = [False, False, False, False, False, False]

tighSpeed = 0.45
kneeSpeed = 0.5
durationTwo = 0
durationOne = 0

def fL_cb(msg):
    global fLPos
    fLPos[0] = msg.tigh
    fLPos[1] = msg.knee
    fLPos[2] = msg.foot

def fR_cb(msg):
    global fRPos
    fRPos[0] = msg.tigh
    fRPos[1] = msg.knee
    fRPos[2] = msg.foot

def mL_cb(msg):
    global mLPos
    mLPos[0] = msg.tigh
    mLPos[1] = msg.knee
    mLPos[2] = msg.foot

def mR_cb(msg):
    global mRPos
    mRPos[0] = msg.tigh
    mRPos[1] = msg.knee
    mRPos[2] = msg.foot

def bL_cb(msg):
    global fLPos
    bLPos[0] = msg.tigh
    bLPos[1] = msg.knee
    bLPos[2] = msg.foot

def bR_cb(msg):
    global fLPos
    bRPos[0] = msg.tigh
    bRPos[1] = msg.knee
    bRPos[2] = msg.foot

def leftSensorTrigger(msg):
    global leftTrigger
    leftTrigger = msg.data

def rightSensorTrigger(msg):
    global rightTrigger
    rightTrigger = msg.data

def getTime(msg):
    global time_now
    time_now = float(msg.data)

def zeroLegs():
    global fLPos
    global fRPos
    global mLPos
    global mRPos

    msg = Leg()
    msg1 = Leg()

    rospy.loginfo("Checking tighs")
    rospy.loginfo(fLPos[0])
    rospy.loginfo(fRPos[0])

    #Tighs

    r = rospy.Rate(50) 

    while fLPos[0] > 0.1 or fLPos[0] < -0.1:
        rospy.loginfo(fLPos[0])
        if fLPos[0] > 0.1:
            msg.tigh = -tighSpeed
            pub[0].publish(msg)
            pub[4].publish(msg)
        elif fLPos[0] < -0.1:
            msg.tigh = tighSpeed
            pub[0].publish(msg)
            pub[4].publish(msg)
        r.sleep()
    msg.tigh = 0
    msg1.tigh = 0
    pub[0].publish(msg)
    pub[4].publish(msg)

    while fRPos[0] > 0.1 or fRPos[0] < -0.1:
        rospy.loginfo(fRPos[0])
        if fRPos[0] > 0.1:
            msg.tigh = -tighSpeed
            pub[1].publish(msg)
            pub[5].publish(msg)
        elif fRPos[0] < -0.1:
            msg.tigh = tighSpeed
            pub[1].publish(msg)
            pub[5].publish(msg)
        r.sleep()
    msg.tigh = 0
    msg1.tigh = 0
    pub[1].publish(msg)
    pub[5].publish(msg)

    #middle legs
    rospy.loginfo("Checking middle legs")

    while mLPos[0] > 0.1 or mLPos[0] < -0.1:
        rospy.loginfo(mLPos[0])
        if mLPos[0] > 0.1:
            msg.tigh = -tighSpeed
            pub[2].publish(msg)
        elif mLPos[0] < -0.1:
            msg.tigh = tighSpeed
            pub[2].publish(msg)
        r.sleep()
    msg.tigh = 0
    pub[2].publish(msg)

    while mRPos[0] > 0.1 or mRPos[0] < -0.1:
        rospy.loginfo(mRPos[0])
        if mRPos[0] > 0.1:
            msg.tigh = -tighSpeed
            pub[3].publish(msg)
        elif mRPos[0] < -0.1:
            msg.tigh = tighSpeed
            pub[3].publish(msg)
        r.sleep()
    msg.tigh = 0
    pub[3].publish(msg)

    #knees and feet
    rospy.loginfo("Checking knees")
    rospy.loginfo(fLPos[1])
    rospy.loginfo(fRPos[1])

    while fLPos[1] > -0.4 or fLPos[1] < -0.65:
        rospy.loginfo(fLPos[1])
        if fLPos[1] > -0.4:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif fLPos[1] < -0.65:
            msg.knee = kneeSpeed
            msg.foot = -kneeSpeed
            pub[0].publish(msg)
            pub[4].publish(msg)
            pub[3].publish(msg)
        r.sleep()
    msg.knee = 0
    msg.foot = 0
    pub[0].publish(msg)
    pub[3].publish(msg)
    pub[4].publish(msg)

    while fRPos[1] > -0.4 or fRPos[1] < -0.65:
        rospy.loginfo(fRPos[1])
        if fRPos[1] > -0.4:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            pub[1].publish(msg)
            pub[5].publish(msg)
            pub[2].publish(msg)
        elif fRPos[1] < -0.65:
            msg.knee = kneeSpeed
            msg.foot = -kneeSpeed
            pub[1].publish(msg)
            pub[5].publish(msg)
            pub[2].publish(msg)
        r.sleep()
    msg.knee = 0
    msg.foot = 0
    pub[1].publish(msg)
    pub[2].publish(msg)
    pub[5].publish(msg)

def turnLeft(c):
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    rospy.loginfo("Left")

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0

    while a == 0:
        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = 0.24
            msg.foot = -0.24
            msg.tigh = -0.20
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
        elif diff >= 1.5 and diff <= 2.78:
            if c > 0:
                msg1.tigh = tighSpeed
                pub[0].publish(msg1)
                pub[3].publish(msg1)
                pub[4].publish(msg1)
            msg.knee = 0
            msg.foot = 0
            msg.tigh = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
        elif diff >= 2.78 and diff <= 4.28:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
        elif diff >= 4.28 and diff <= 5.28:
            msg.knee = 0
            msg.foot = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            break
        r.sleep()

def turnLefter():
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0
    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = 0.24
            msg.foot = -0.24
            msg.tigh = -0.20
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 1.5 and diff <= 2.78:
            msg.knee = 0
            msg.foot = 0
            msg.tigh = 0
            msg1.tigh = tighSpeed
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            pub[1].publish(msg1)
            pub[2].publish(msg1)
            pub[5].publish(msg1)
        elif diff >= 2.78 and diff <= 4.28:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            msg1.tigh = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            pub[1].publish(msg1)
            pub[2].publish(msg1)
            pub[5].publish(msg1)
        elif diff >= 4.28 and diff <= 5.28:
            msg.knee = 0
            msg.foot = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            break
        r.sleep()

def finishLeft():
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0
    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = -0.25
            msg.foot = 0.25
            msg.tigh = 0.20
            msg1.knee = -0.25
            msg1.foot = 0.25
            msg1.tigh = 0.20
            pub[0].publish(msg)
            pub[3].publish(msg1)
            pub[4].publish(msg)
        elif diff >= 1.5 and diff <= 3:
            msg.knee = kneeSpeed
            msg.foot = -kneeSpeed
            msg.tigh = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 3 and diff <= 4:
            msg.knee = 0
            msg.foot = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            break
        r.sleep()  

def turnRight(c):
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    rospy.loginfo("Right")

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0

    while a == 0:
        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = 0.25
            msg.foot = -0.25
            msg.tigh = 0.20
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 1.5 and diff <= 2.78:
            if c > 0:
                msg1.tigh = -tighSpeed
                pub[1].publish(msg1)
                pub[2].publish(msg1)
                pub[5].publish(msg1)
            msg.knee = 0
            msg.foot = 0
            msg.tigh = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 2.78 and diff <= 4.28:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 4.28 and diff <= 5.28:
            msg.knee = 0
            msg.foot = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            break
        r.sleep()

def turnRighter():
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0
    while a == 0:
        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = 0.25
            msg.foot = -0.25
            msg.tigh = 0.20
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
        elif diff >= 1.5 and diff <= 2.78:
            msg.knee = 0
            msg.foot = 0
            msg.tigh = 0
            msg1.tigh = -tighSpeed
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            pub[0].publish(msg1)
            pub[3].publish(msg1)
            pub[4].publish(msg1)
        elif diff >= 2.78 and diff <= 4.28:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            msg1.tigh = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            pub[0].publish(msg1)
            pub[3].publish(msg1)
            pub[4].publish(msg1)
        elif diff >= 4.28 and diff <= 5.28:
            msg.knee = 0
            msg.foot = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            break
        r.sleep()

def finishRight():
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0
    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()
        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = -0.25
            msg.foot = 0.25
            msg.tigh = -0.20
            msg1.knee = -0.25
            msg1.foot = 0.25
            msg1.tigh = -0.20
            pub[1].publish(msg)
            pub[2].publish(msg1)
            pub[5].publish(msg)
        elif diff >= 1.5 and diff <= 3:
            msg.knee = kneeSpeed
            msg.foot = -kneeSpeed
            msg.tigh = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
        elif diff >= 3 and diff <= 4:
            msg.knee = 0
            msg.foot = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            break
        r.sleep() 

def finishWalk():
    global time_now
    r = rospy.Rate(50)
    diff = 0.0

    rospy.loginfo("finish")

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0

    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()

        diff = time_now - current_time

        if diff <= 1.5:
            msg.knee = 0.25
            msg.foot = -0.25
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
        elif diff >= 1.5 and diff <= 2.78:
            msg2.knee = 0
            msg2.foot = 0
            msg.tigh = 0.25
            msg1.tigh = -0.25
            pub[0].publish(msg2)
            pub[3].publish(msg2)  
            pub[4].publish(msg2)
            pub[1].publish(msg)
            pub[5].publish(msg)
            pub[2].publish(msg1)
        elif diff >= 2.78 and diff <= 3.53:
            msg1.tigh = 0
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            pub[1].publish(msg1)
            pub[5].publish(msg1)
            pub[2].publish(msg1)
        elif diff >= 3.53 and diff <= 4.53:
            msg.knee = 0
            msg.foot = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            break
        r.sleep()

def stepOne(c):
    global durationOne
    global durationTwo
    global time_now
    r = rospy.Rate(50)
    diff = 0.0
    x = 0

    rospy.loginfo("Waiting...")

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0

    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()

        diff = time_now - current_time
        if diff <= 1.5:
            msg.knee = 0.25
            msg.foot = -0.25
            msg.tigh = 0.20
            msg1.tigh = -0.20
            msg1.knee = 0.25
            msg1.foot = -0.25
            pub[0].publish(msg)
            pub[3].publish(msg1)
            pub[4].publish(msg)
            durationOne = 2.78
            x = durationOne + 1.5
        elif diff >= 1.5 and diff <= durationOne:
            if c > 0:    
                msg2.tigh = -tighSpeed
                msg.tigh = tighSpeed
            msg1.knee = 0
            msg1.foot = 0
            msg1.tigh = 0
            pub[0].publish(msg1)
            pub[3].publish(msg1)
            pub[4].publish(msg1)
            pub[1].publish(msg)
            pub[2].publish(msg2)
            pub[5].publish(msg)
        elif diff >= durationOne and diff <= x:
            msg.tigh = 0
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            msg1.tigh = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            pub[1].publish(msg1)
            pub[2].publish(msg1)
            pub[5].publish(msg1)
        elif diff >= x and diff <= 6.78:
            msg.knee = 0
            msg.foot = 0
            pub[0].publish(msg)
            pub[3].publish(msg)
            pub[4].publish(msg)
            break
        r.sleep()

def stepTwo():
    global kneeSpeed
    global durationOne
    global durationTwo
    global time_now
    r = rospy.Rate(50)
    diff = 0.0
    x = 0

    rospy.loginfo("Walking...")

    while time_now == 0:
        current_time = 0.0
    current_time = time_now

    a = 0

    while a == 0:

        msg = Leg()
        msg1 = Leg()
        msg2 = Leg()
        msg3 = Leg()

        diff = time_now - current_time
        if diff <= 1.5:
            msg1.tigh = 0.20
            msg1.knee = 0.25
            msg1.foot = -0.25
            msg.tigh = -0.20
            msg.knee = 0.25
            msg.foot = -0.25
            pub[1].publish(msg)
            pub[2].publish(msg1)
            pub[5].publish(msg)
            durationTwo = 2.78
            x = durationTwo + 1.5
        elif diff >= 1.5 and diff <= durationTwo:
            msg.tigh = 0
            msg.knee = 0
            msg.foot = 0
            msg1.tigh = tighSpeed
            msg2.tigh = -tighSpeed
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            pub[0].publish(msg2)
            pub[3].publish(msg1)
            pub[4].publish(msg2)
        elif diff >= durationTwo and diff <= x:
            msg.knee = -kneeSpeed
            msg.foot = kneeSpeed
            msg1.tigh = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            pub[0].publish(msg1)
            pub[3].publish(msg1)
            pub[4].publish(msg1)
        elif diff >= x and diff <= 6.78:
            msg.knee = 0
            msg.foot = 0
            pub[1].publish(msg)
            pub[2].publish(msg)
            pub[5].publish(msg)
            break
        r.sleep()

if __name__ == '__main__':

    rospy.Subscriber('/sysTimeTopic', Float32, getTime)
    rospy.Subscriber('/leftSensor', Bool, leftSensorTrigger)
    rospy.Subscriber('/rightSensor', Bool, rightSensorTrigger)
    rospy.Subscriber('/frontLeftPos', Leg, fL_cb)
    rospy.Subscriber('/frontRightPos', Leg, fR_cb)
    rospy.Subscriber('/middleLeftPos', Leg, mL_cb)
    rospy.Subscriber('/middleRightPos', Leg, mR_cb)
    rospy.Subscriber('/backLeftPos', Leg, bL_cb)
    rospy.Subscriber('/backRightPos', Leg, bR_cb)

    a = 0

    r = rospy.Rate(50)

    while not rospy.is_shutdown():

        rospy.loginfo(leftTrigger)
        rospy.loginfo(rightTrigger)
        
        if leftTrigger == False and rightTrigger == False:
            b = 0
            while leftTrigger == False and rightTrigger == False:
                stepOne(b)
                stepTwo()
                c = b % 3
                if c == 0:
                    zeroLegs()
                b = b + 1
            finishWalk()
        elif leftTrigger == False and rightTrigger == True:
            b = 0
            while leftTrigger == False and rightTrigger == True:
                turnLeft(b)
                turnLefter()
                c = b % 3
                if c == 0:
                    zeroLegs()
                b = b + 1
            finishLeft()
        elif leftTrigger == True and rightTrigger == False:
            b = 0
            while leftTrigger == True and rightTrigger == False:
                turnRight(b)
                turnRighter()
                c = b % 3
                if c == 0:
                    zeroLegs()
                b = b + 1
            finishRight()
        elif leftTrigger == True and rightTrigger == True:
            b = 0
            while leftTrigger == True and rightTrigger == True:
                turnRight(b)
                turnRighter()
                c = b % 3
                if c == 0:
                    zeroLegs()
                b = b + 1
            finishRight()
        zeroLegs()
        r.sleep()