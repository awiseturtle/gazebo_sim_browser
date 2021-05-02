#!/usr/bin/env python3
## python was changed to python3 in this line, because of the error(https://stackoverflow.com/questions/63054393/failed-to-launch-rospy-file-syntaxerror-invalid-syntax-yamlobjectmetaclass-ya)

import rospy
from geometry_msgs.msg import Twist
# from std_msgs.msg import Float64
# import math

def talker():
    rospy.init_node('vel_publisher')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)
    move = Twist() # defining the way we can allocate the values
    move.linear.x = 0.5 # allocating the values in x direction - linear
    move.angular.z = 0.0  # allocating the values in z direction - angular

    while not rospy.is_shutdown():
      pub.publish(move)
      rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
