#!/usr/bin/env python3

import rospy
import roslib
import serial 
from std_msgs.msg import String

# port = "ИМЯ ПОРТА СТМКИ С ДВИГАТЕЛЕМ"
# mySerialPort = serial.Serial(port)

def callback(data):
    print(data)
     # mySerialPort.write(data.data.encode())

rospy.init_node("stm_transporter")
rospy.Subscriber("transporter_topic", String, callback)
rospy.spin()
# mySerialPort.close()
