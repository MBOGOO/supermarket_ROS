#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class RobotController:
    def __init__(self):
        rospy.init_node("robot_controller")

        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)

        self.x = 0
        self.y = 0

    def get_speed(self, position):
        # Innovation: speed depends on "aisle width"
        if abs(position) < 2:
            return 0.2   # narrow aisle → slow
        else:
            return 0.6   # wide aisle → fast

    def move(self):
        while not rospy.is_shutdown():
            twist = Twist()

            speed = self.get_speed(self.x)

            twist.linear.x = speed
            twist.angular.z = 0.1  # slight correction (DWA-like)

            self.pub.publish(twist)

            self.x += 0.1

            rospy.loginfo(f"Position: {self.x:.2f}, Speed: {speed}")

            self.rate.sleep()

if __name__ == "__main__":
    robot = RobotController()
    robot.move()
