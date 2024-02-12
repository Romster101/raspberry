#!/usr/bin/env python3

import rospy
import roslib
import serial 
from std_msgs.msg import String

port = "/dev/ttyACM0"
mySerialPort = serial.Serial(port)

def callback(data):
     mySerialPort.write(data.data.encode())

rospy.init_node("stm_transmit")
rospy.Subscriber("wheel_Vel_Target", String, callback)
rospy.spin()
mySerialPort.close()
