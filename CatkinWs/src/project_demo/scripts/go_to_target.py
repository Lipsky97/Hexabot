#! /usr/bin/env python

# A program developed by Oskar Lipienski for the purpose of Major Project
# Development of hexapod robotic systems

# The program robot will start from cell 1,1 and plot a way to the goal
# cell that can be set in the argument for producePath() function. After
# entering the new cell the robot will update the map with locations 
# of sensed obstacles, then generate a repulsive field map of the environment,
# and plot a path, which is a list of commands for the robot. It is using a
# custom message type "Leg" that consists of 3 float32 variables. It has been 
# created to help control velocities of each motor in each leg.
# Final Version

import rospy
import actionlib
from rospy.numpy_msg import numpy_msg
import numpy as np
from project_demo.msg import Leg
from std_msgs.msg import Float32, Bool

# Initiate new ROS node
rospy.init_node("map_and_locate")

# Create plublisher for each leg
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

# Global variable for system time
time_now = 0.0

# Global variables for speeds of particular parts of the leg
tighSpeed = 1
kneeSpeed = 0.5

# Starting coordinates
x = 1
y = 1
current = [x, y]

# Orientation of the robot relative to the fixed directions
# 0 = east
# 1 = south
# 2 = west
# 4 = north
rotation = 0

# List of commands to get to the goal
moveStack = []

# Map of all obstacles
freeSpace = np.zeros((11,11), dtype=np.float32)
# Map of repulsive fields
obstacleSpace = np.zeros((11,11), dtype=np.float32)

# Proximity sensors
# front = [front, right, left]
# back = [back, right, left]
frontProx = [0, 0, 0]
backProx = [0, 0, 0]

# Leg positions
fLPos = [0, 0, 0]
fRPos = [0, 0, 0]
mLPos = [0, 0, 0]
mRPos = [0, 0, 0]
bLPos = [0, 0, 0]
bRPos = [0, 0, 0]

# -----------------Callback functions for proximity sensors, leg positions, and system time-----------------
def fProx_cb(msg):
    global frontProx
    frontProx[0] = msg.tigh
    frontProx[1] = msg.knee
    frontProx[2] = msg.foot

def bProx_cb(msg):
    global backProx
    backProx[0] = msg.tigh
    backProx[1] = msg.knee
    backProx[2] = msg.foot

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

def getTime(msg):
    global time_now
    time_now = float(msg.data)

# ---------------Behaviours-----------------
def liftLeg(i):
    # i = number of a leg
    msg = Leg()
    msg.knee = -kneeSpeed
    msg.foot = kneeSpeed

    if i == 0:
        while fLPos[1] > -0.85:
            pub[i].publish(msg)
    elif i == 1:
        while fRPos[1] > -0.85:
            pub[i].publish(msg)
    elif i == 2:
        while mLPos[1] > -0.85:
            pub[i].publish(msg)
    elif i == 3:
        while mRPos[1] > -0.85:
            pub[i].publish(msg)
    elif i == 4:
        while bLPos[1] > -0.85:
            pub[i].publish(msg)
    elif i == 5:
        while bRPos[1] > -0.85:
            pub[i].publish(msg)
    stopLegs()

def legDown(i):
    # i = number of a leg
    global fLPos
    global fRPos
    global mLPos
    global mRPos
    global bLPos
    global bRPos
    global legTouch
    msg = Leg()
    msg.knee = kneeSpeed
    msg.foot = -kneeSpeed

    if i == 0:
        while fLPos[1] < -0.52:
            pub[i].publish(msg)
    elif i == 1:
        while fRPos[1] < -0.52:
            pub[i].publish(msg)
    elif i == 2:
        while mLPos[1] < -0.52:
            pub[i].publish(msg)
    elif i == 3:
        while mRPos[1] < -0.52:
            pub[i].publish(msg)
    elif i == 4:
        while bLPos[1] < -0.52:
            pub[i].publish(msg)
    elif i == 5:
        while bRPos[1] < -0.52:
            pub[i].publish(msg)
    stopLegs()

# ZeroLegs() will check if all leg motors are at the right initial position
# helps reduce error introduced by walking and turning
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

    liftLeg(0)
    liftLeg(4)

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

    legDown(0)
    legDown(4)
    liftLeg(1)
    liftLeg(5)

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

    legDown(1)
    legDown(5)

    #middle legs
    rospy.loginfo("Checking middle legs")

    liftLeg(2)

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

    legDown(2)
    liftLeg(3)

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

    legDown(3)

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

def stopLegs():
    msg = Leg()

    msg.tigh = 0
    msg.knee = 0
    msg.foot = 0
    msg.tigh = 0
    msg.knee = 0
    msg.foot = 0
    pub[0].publish(msg)
    pub[4].publish(msg)
    pub[3].publish(msg)
    pub[1].publish(msg)
    pub[5].publish(msg)
    pub[2].publish(msg)

# Function responsible for walk action. It is using joint positions to determine
# if the leg has made a move. It can be looped any amount of times thanks to the
# if fRPos[0] <= -0.1 statement. The robot will retract the legs if they are not at
# starting position. It is using the tripod gait.
def walk():
    global fLPos
    global fRPos
    global mLPos
    global mRPos
    global legTouch

    rospy.loginfo("Walking forward...")

    r = rospy.Rate(50)

    while fLPos[1] == 0 or fRPos[1] == 0 or fLPos[0] == 0 or fRPos[0] == 0:
        s = 0

    while fLPos[0] <= 0.3:
        msg = [Leg(), Leg(), Leg(), Leg()]
        if fRPos[0] <= -0.1:
            msg[2].tigh = tighSpeed
            msg[3].tigh = -tighSpeed
            pub[1].publish(msg[2])
            pub[5].publish(msg[2])
            pub[2].publish(msg[3])
        msg[0].tigh = tighSpeed
        msg[0].knee = kneeSpeed
        msg[0].foot = -kneeSpeed
        msg[1].tigh = -tighSpeed
        msg[1].knee = kneeSpeed
        msg[1].foot = -kneeSpeed
        pub[0].publish(msg[0])
        pub[4].publish(msg[0])
        pub[3].publish(msg[1])
    stopLegs()
    while fRPos[0] <= -0.1:
        msg = [Leg(), Leg()]
        msg[0].tigh = tighSpeed
        msg[1].tigh = -tighSpeed
        pub[1].publish(msg[0])
        pub[5].publish(msg[0])
        pub[2].publish(msg[1])
    stopLegs()
    while fLPos[1] > -0.52:
        msg = [Leg(), Leg(), Leg(), Leg()]
        msg[0].knee = -kneeSpeed
        msg[0].foot = kneeSpeed
        msg[1].knee = -kneeSpeed
        msg[1].foot = kneeSpeed
        pub[0].publish(msg[0])
        pub[4].publish(msg[0])
        pub[3].publish(msg[1])
    stopLegs()
    while fRPos[0] >= -0.3:
        msg = [Leg(), Leg(), Leg(), Leg()]
        if fLPos[0] >= 0.1:
            msg[2].tigh = -tighSpeed
            msg[3].tigh = tighSpeed
            pub[0].publish(msg[2])
            pub[4].publish(msg[2])
            pub[3].publish(msg[3])
        msg[0].tigh = -tighSpeed
        msg[0].knee = kneeSpeed
        msg[0].foot = -kneeSpeed
        msg[1].tigh = tighSpeed
        msg[1].knee = kneeSpeed
        msg[1].foot = -kneeSpeed    
        pub[1].publish(msg[0])
        pub[5].publish(msg[0])
        pub[2].publish(msg[1])
    stopLegs()
    while fRPos[0] >= 0.1:
        msg = [Leg(), Leg()]
        msg[0].tigh = -tighSpeed
        msg[1].tigh = tighSpeed
        pub[0].publish(msg[0])
        pub[4].publish(msg[0])
        pub[3].publish(msg[1])
    stopLegs()
    while fRPos[1] > -0.52:
        msg = [Leg(), Leg(), Leg(), Leg()]
        msg[0].knee = -kneeSpeed
        msg[0].foot = kneeSpeed
        msg[1].knee = -kneeSpeed
        msg[1].foot = kneeSpeed
        pub[1].publish(msg[0])
        pub[5].publish(msg[0])
        pub[2].publish(msg[1])
    stopLegs()

# Used for turning Right. The function is using the gait with 5 points of contact with the
# ground to provide more reliable angles of turning. The rest is similar to the walk() funciton.
def spinRight():
    global fLPos
    global fRPos
    global mLPos
    global mRPos
    global bLPos
    global bRPos

    msg = Leg()
    msg1 = Leg()
    msg.tigh = -tighSpeed
    msg1.tigh = tighSpeed

    rospy.loginfo("Spin Right...")

    liftLeg(0)
    while fLPos[0] >= -0.45:
        pub[0].publish(msg)
    stopLegs()
    legDown(0)
    liftLeg(1)
    while fRPos[0] >= -0.45:
        pub[1].publish(msg)
    stopLegs()
    legDown(1)
    liftLeg(2)
    while mLPos[0] >= -0.45:
        pub[2].publish(msg)
    stopLegs()
    legDown(2)
    liftLeg(3)
    while mRPos[0] >= -0.45:
        pub[3].publish(msg)
    stopLegs()
    legDown(3)
    liftLeg(4)
    while bLPos[0] >= -0.45:
        pub[4].publish(msg)
    stopLegs()
    legDown(4)
    liftLeg(5)
    while bRPos[0] >= -0.45:
        pub[5].publish(msg)
    stopLegs()
    legDown(5)

    while fLPos[0] <= -0.1:
        pub[0].publish(msg1)
        pub[2].publish(msg1)
        pub[4].publish(msg1)
        pub[1].publish(msg1)
        pub[3].publish(msg1)
        pub[5].publish(msg1)
    stopLegs()

# Identiacal to the spinRight() except for turning left
def spinLeft():
    global fLPos
    global fRPos
    global mLPos
    global mRPos
    global bLPos
    global bRPos

    msg = Leg()
    msg1 = Leg()
    msg.tigh = tighSpeed
    msg1.tigh = -tighSpeed

    rospy.loginfo("Spin Left...")

    liftLeg(0)
    while fLPos[0] <= 0.45:
        pub[0].publish(msg)
    stopLegs()
    legDown(0)
    liftLeg(1)
    while fRPos[0] <= 0.45:
        pub[1].publish(msg)
    stopLegs()
    legDown(1)
    liftLeg(2)
    while mLPos[0] <= 0.45:
        pub[2].publish(msg)
    stopLegs()
    legDown(2)
    liftLeg(3)
    while mRPos[0] <= 0.45:
        pub[3].publish(msg)
    stopLegs()
    legDown(3)
    liftLeg(4)
    while bLPos[0] <= 0.45:
        pub[4].publish(msg)
    stopLegs()
    legDown(4)
    liftLeg(5)
    while bRPos[0] <= 0.45:
        pub[5].publish(msg)
    stopLegs()
    legDown(5)

    while fLPos[0] >= 0.1:
        pub[0].publish(msg1)
        pub[2].publish(msg1)
        pub[4].publish(msg1)
        pub[1].publish(msg1)
        pub[3].publish(msg1)
        pub[5].publish(msg1)
    stopLegs()

def oneCellForward():
    walk()
    walk()
    walk()
    walk()
    walk()

def leftAndForward():
    spinLeft()
    spinLeft()
    spinLeft()
    spinLeft()
    spinLeft()
    oneCellForward()

def rightAndForward():
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    oneCellForward()    

def trunAround():
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    spinRight()
    oneCellForward()

# -------------Location and Mapping---------------

# This will check the proximity sensors around the robot and update map in case 
# any new obstacles have been detected. The orientation of the robot has to be checked
# in order match right reading to the fixed world direction
def updateMap():
    global frontProx
    global backProx
    global freeSpace
    global x
    global y

    a = 0.5
    freeSpace[x,y] = 1

    if rotation == 0: #east
        if frontProx[2] < a and frontProx[2] > 0:
            freeSpace[x-1,y] = -1
        if frontProx[2] > a:
            freeSpace[x-2,y] = -1
        if frontProx[0] < a and frontProx[0] > 0:
            freeSpace[x, y+1] = -1
        if frontProx[0] > a:
            freeSpace[x, y+2] = -1
        if frontProx[1] < a and frontProx[1] > 0:
            freeSpace[x+1,y] = -1
        if frontProx[1] > a:
            freeSpace[x+2,y] = -1
        if backProx[0] < a and backProx[0] > 0:
            freeSpace[x,y-1] = -1
        if backProx[0] > a:
            freeSpace[x,y-2] = -1
    elif rotation == 1: #south
        if frontProx[2] < a and frontProx[2] > 0:
            freeSpace[x,y+1] = -1
        if frontProx[2] > a:
            freeSpace[x,y+2] = -1
        if frontProx[0] < a and frontProx[0] > 0:
            freeSpace[x+1, y] = -1
        if frontProx[0] > a:
            freeSpace[x+2, y] = -1
        if frontProx[1] < a and frontProx[1] > 0:
            freeSpace[x,y-1] = -1
        if frontProx[1] > a:
            freeSpace[x,y-2] = -1
        if backProx[0] < a and backProx[0] > 0:
            freeSpace[x-1,y] = -1
        if backProx[0] > a:
            freeSpace[x-2,y] = -1
    elif rotation == 2: #west
        if frontProx[2] < a and frontProx[2] > 0:
            freeSpace[x+1,y] = -1
        if frontProx[2] > a:
            freeSpace[x+2,y] = -1
        if frontProx[0] < a and frontProx[0] > 0:
            freeSpace[x, y-1] = -1
        if frontProx[0] > a:
            freeSpace[x, y-2] = -1
        if frontProx[1] < a and frontProx[1] > 0:
            freeSpace[x-1,y] = -1
        if frontProx[1] > a:
            freeSpace[x-2,y] = -1
        if backProx[0] < a and backProx[0] > 0:
            freeSpace[x,y+1] = -1
        if backProx[0] > a:
            freeSpace[x,y+2] = -1
    elif rotation == 3: #north
        if frontProx[2] < a and frontProx[2] > 0:
            freeSpace[x,y-1] = -1
        if frontProx[2] > a:
            freeSpace[x,y-2] = -1
        if frontProx[0] < a and frontProx[0] > 0:
            freeSpace[x-1, y] = -1
        if frontProx[0] > a:
            freeSpace[x-1, y] = -1
        if frontProx[1] < a and frontProx[1] > 0:
            freeSpace[x,y+1] = -1
        if frontProx[1] > a:
            freeSpace[x,y+2] = -1
        if backProx[0] < a and backProx[0] > 0:
            freeSpace[x+1,y] = -1
        if backProx[0] > a:
            freeSpace[x+2,y] = -1
    rospy.loginfo(freeSpace)

def updateLocation(i):
    # i = direction in which the robot has moved
    global x
    global y

    if i == 0: #+x
        x = x + 1
    elif i == 1: #-x
        x = x - 1
    elif i == 2: #+y
        y = y + 1
    elif i == 3: #-y
        y = y - 1

# It will make sure robot will stay in line with an absolute world direction
def alignToWall():
    global frontProx
    global backProx

    rospy.loginfo("Aligning")
    
    if frontProx[2] <= 0.3:
        diff = frontProx[2] - backProx[2]
        if diff > 0.025:
            spinLeft()
            zeroLegs()
        elif diff < -0.02:
            spinRight()
            zeroLegs()
    if frontProx[1] <= 0.3:
        diff = frontProx[1] - backProx[1]
        if diff >= 0.025:
            spinRight()
            zeroLegs()
        elif diff <= -0.02:
            spinLeft()
            zeroLegs()

# Function that translates the freeSpace map of obstacles to the map of repulsive fields
# It is looking at all the surrounding cells to determine what value to assign to the current
# cell. The downside of the function is the fact the map is only translated once which results in
# fields stronger around upper-left side of the obstacles.
def translateMap():
    global freeSpace
    global obstacleSpace
    rows = freeSpace.shape[0]
    cols = freeSpace.shape[1]

    for x in range(0, cols):
        for y in range(0, rows):
            obstacleSpace[x,y] = freeSpace[x,y]
    
    rows = obstacleSpace.shape[0]
    cols = obstacleSpace.shape[1]

    for x in range(1, 10):
        for y in range(1, 10):
            cells = [obstacleSpace[x-1,y-1], obstacleSpace[x-1,y+1], obstacleSpace[x+1,y-1], 
            obstacleSpace[x+1,y+1], obstacleSpace[x-1,y], obstacleSpace[x+1,y], 
            obstacleSpace[x,y+1], obstacleSpace[x,y-1]]

            smallest = 20
            present = False
            for i in cells:
                if i == -1:
                    present = True
                if i < smallest and i != 0:
                    smallest = i

            if present == True and obstacleSpace[x,y] != -1:
                obstacleSpace[x,y] = 2
            elif present == False and obstacleSpace[x,y] != -1:
                obstacleSpace[x,y] = smallest+1

# Here the program will find a path to the cell[xt,yt]. The algorithm starts from the
# goal cell and, using the repulsive fields map, attempts to find a path to the present 
# position of the robot. The algorithm will attempt to find a path using everithing the 
# robot has sensed. The algorithm will also notify the user in case no valid path have been
# found or in case it got stuck at some point. As the algorithm is marking path it has took
# with 0's on xpathSpace it is also saving every step it has made in moveStack list.
def producePath(xt, yt):
    # xt = target x coordinate
    # yt = target y coordinate
    global x
    global y
    global obstacleSpace
    global moveStack

    rows = obstacleSpace.shape[0]
    cols = obstacleSpace.shape[1]

    xpathSpace = np.zeros((11,11), dtype=np.float32)

    for xe in range(0, cols):
        for ye in range(0, rows):
            xpathSpace[xe,ye] = obstacleSpace[xe,ye]


    lastX = 0
    lastY = 0

    del moveStack[:]

    while x != xt or y != yt:

        if lastX==xt and lastY==yt:
            rospy.loginfo("stuck at:")
            rospy.loginfo(xt)
            rospy.loginfo(yt)
            break
        lastX=xt
        lastY=yt

        xpathSpace[xt,yt] = 0
        if x < xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[2] > 1:
                    moveStack.append(2)
                    yt = yt + 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x < xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x > xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
                elif xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x > xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
                elif xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x == xt and y < yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
                elif xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x == xt and y > yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x < xt and y == yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
                elif xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
        elif x > xt and y == yt:
            xcells = [xpathSpace[xt-1,yt], xpathSpace[xt,yt+1], 
            xpathSpace[xt+1,yt], xpathSpace[xt,yt-1]]

            biggest = 0
            for i in xcells:
                if i > biggest:
                    biggest = i

            if biggest > 1:
                if xcells[2] > 1:
                    moveStack.append(3)
                    xt = xt + 1
                elif xcells[3] > 1:
                    moveStack.append(0)
                    yt = yt - 1
                elif xcells[1] > 1:
                    moveStack.append(2)
                    yt = yt + 1
                elif xcells[0] > 1:
                    moveStack.append(1)
                    xt = xt - 1
            else:
                rospy.loginfo("stuck")
                del moveStack[:]
    rospy.loginfo(xpathSpace)
    rospy.loginfo(moveStack)

# This function will use moveStack list produced by producePath() function and translate
# the list of nubers to the commands for a robot to follow. Ech number means an absolut direction
# in which the robot should go on the grid, so the orientation of the robot has to be checked to
# create a list of viable commands.
def followPath():
    global rotation, x, y
    global moveStack

    if len(moveStack) != 0:

        if rotation == 0:
            if moveStack[-1] == 0:
                oneCellForward()
                updateLocation(2)
            elif moveStack[-1] == 1:
                rightAndForward()
                updateLocation(0)
            elif moveStack[-1] == 2:
                trunAround()
                updateLocation(3)
            elif moveStack[-1] == 3:
                leftAndForward()
                updateLocation(1)

        elif rotation == 1:
            if moveStack[-1] == 0:
                leftAndForward()
                updateLocation(2)
            elif moveStack[-1] == 1:
                oneCellForward()
                updateLocation(0)
            elif moveStack[-1] == 2:
                rightAndForward()
                updateLocation(3)
            elif moveStack[-1] == 3:
                trunAround()
                updateLocation(1)
        
        elif rotation == 2:
            if moveStack[-1] == 0:
                trunAround()
                updateLocation(2)
            elif moveStack[-1] == 1:
                leftAndForward()
                updateLocation(0)
            elif moveStack[-1] == 2:
                oneCellForward()
                updateLocation(3)
            elif moveStack[-1] == 3:
                rightAndForward()
                updateLocation(1)
        
        elif rotation == 3:
            if moveStack[-1] == 0:
                rightAndForward()
                updateLocation(2)
            elif moveStack[-1] == 1:
                trunAround()
                updateLocation(0)
            elif moveStack[-1] == 2:
                leftAndForward()
                updateLocation(3)
            elif moveStack[-1] == 3:
                oneCellForward()
                updateLocation(1)

        moveStack.pop()

        rospy.loginfo("At the target")

if __name__ == '__main__':

    # subscribers for simulation time and proximity sensors
    rospy.Subscriber('/sysTimeTopic', Float32, getTime)
    rospy.Subscriber('/frontProx', Leg, fProx_cb)
    rospy.Subscriber('/backProx', Leg, bProx_cb)
    # leg positions
    rospy.Subscriber('/frontLeftPos', Leg, fL_cb)
    rospy.Subscriber('/frontRightPos', Leg, fR_cb)
    rospy.Subscriber('/middleLeftPos', Leg, mL_cb)
    rospy.Subscriber('/middleRightPos', Leg, mR_cb)
    rospy.Subscriber('/backLeftPos', Leg, bL_cb)
    rospy.Subscriber('/backRightPos', Leg, bR_cb)

    # The main algorithm will first make sure all legs are at the starting position,
    # then update the map with all the obstacles that can be sensed at the time,
    # next it will translate the map of obstacles to the repulsive fields map, plot the
    # path to the set goal and follow it. After the robot will relocate one cell in x or y
    # direction and it will check if it can align itself with any wall to make sure it stays
    # in line with absolute north, west, east, or south. The process is repeated until the robot
    # is at the target.

    r = rospy.Rate(50)
    zeroLegs()
    while not rospy.is_shutdown():
        updateMap()
        translateMap()
        producePath(8, 3)
        followPath()
        alignToWall()
        rospy.loginfo(rotation)
        rospy.loginfo(obstacleSpace)
        r.sleep()