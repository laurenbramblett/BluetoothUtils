
"""PyBluez listening via text file and ROS application

Simple demonstration of reading from a text file and sending command via ROS message.

Author: Lauren Bramblett
"""

import bluetooth
import rospy
from geometry_msgs.msg import Twist
import math as m

class robot:
	def __init__(self):
		self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

if __name__=="__main__":
    rospy.init_node("read", anonymous=True)
    Hz = 10
    rate = rospy.Rate(Hz)
    jackal = robot()
    twist = Twist()
    
    while not rospy.is_shutdown():
        line = open('data.txt', 'r')
        data = line.read().rstrip()
        if data == "Spin":
            print('your mom')
            twist.angular.z = m.pi/6
        else:
            print('nah')
            twist.angular.z = 0
        jackal.vel_pub.publish(twist)
        rate.sleep()

