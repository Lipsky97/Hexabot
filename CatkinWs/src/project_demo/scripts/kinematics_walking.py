#! /usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Float32, Bool
from control_msgs.msg import (FollowJointTrajectoryAction,
                              FollowJointTrajectoryGoal)
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from moveit_msgs.msg import MoveItErrorCodes
from moveit_python import MoveGroupInterface, PlanningSceneInterface
from geometry_msgs.msg import Twist, PoseStamped, Pose, Point, Quaternion

rospy.init_node("kin_walk")

move_group1 = MoveGroupInterface("frontLeftLeg", "body")
move_group2 = MoveGroupInterface("frontRightLeg", "body")

planning_scene = PlanningSceneInterface("body")

joint_names_fL = ["tigh_joint", "knee_joint", "foot_joint"]
joint_names_fR = ["tigh_joint2", "knee_joint2", "foot_joint2"]

start_pose = [[0.0, -0.6, 1.2]]
give_left_paw = [[-1.024, -1.4059, -0.521]]
give_right_paw = [[1.3364, -0.9893, 0.0521]]

def give_paw():
    for pose in start_pose:
        if rospy.is_shutdown():
            break
        move_group1.moveToJointPosition(joint_names_fL, pose, wait=False)

        move_group1.get_move_action().wait_for_result()
        result = move_group1.get_move_action().get_result()

        if result:
            if result.error_code.val == MoveItErrorCodes.SUCCESS:
                rospy.loginfo("Done")
            else:
                rospy.logerr("Leg goal in state: %s", 
                move_group1.get_move_action().get_state())
    move_group1.get_move_action().cancel_all_goals()

    for pose in start_pose:
        if rospy.is_shutdown():
            break
        move_group2.moveToJointPosition(joint_names_fR, pose, wait=False)

        move_group2.get_move_action().wait_for_result()
        result = move_group2.get_move_action().get_result()

        if result:
            if result.error_code.val == MoveItErrorCodes.SUCCESS:
                rospy.loginfo("Done")
            else:
                rospy.logerr("Leg goal in state: %s", 
                move_group2.get_move_action().get_state())
    move_group2.get_move_action().cancel_all_goals()

if __name__ == '__main__':
    give_paw()
