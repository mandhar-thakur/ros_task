#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def move_turtle_rectangle(length, breadth):
    rospy.init_node('move_turtle_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    vel_msg = Twist()

    # Set the desired speed and turn rate
    forward_speed = 0.5
    turn_speed = 0.5  # Adjust for 90-degree turns

    def move_straight(distance):
        vel_msg.linear.x = forward_speed
        vel_msg.angular.z = 0.0
        distance_traveled = 0.0
        while distance_traveled < distance and not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            distance_traveled += forward_speed / 10  # Approximate distance traveled in one cycle
            rate.sleep()
        vel_msg.linear.x = 0.0  # Stop the forward motion
        velocity_publisher.publish(vel_msg)

    def turn_90_degrees():
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = turn_speed
        angle_turned = 0.0
        turn_duration = 1.57 / turn_speed  # Approximate time for a 90-degree turn
        start_time = time.time()
        while (time.time() - start_time) < turn_duration and not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            rate.sleep()
        vel_msg.angular.z = 0.0  # Stop turning
        velocity_publisher.publish(vel_msg)

    rospy.loginfo("Moving the turtle in a rectangle...")

    while not rospy.is_shutdown():
        # Move forward along length
        move_straight(length)
        # Turn 90 degrees
        turn_90_degrees()
        # Move forward along breadth
        move_straight(breadth)
        # Turn 90 degrees
        turn_90_degrees()
        # Move forward along length
        move_straight(length)
        # Turn 90 degrees
        turn_90_degrees()
        # Move forward along breadth
        move_straight(breadth)
        # Turn 90 degrees to return to initial orientation
        turn_90_degrees()

if __name__ == '__main__':
    try:
        length = 2.0  # Adjust the desired length
        breadth = 1.0  # Adjust the desired breadth
        move_turtle_rectangle(length, breadth)
    except rospy.ROSInterruptException:
        pass
