#!/usr/bin/env python
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import Float32

BUZZER = 19
pwmPin = None

def callback(data):
    rospy.loginfo("Duration: " + str(data.data))
    pwmPin = GPIO.PWM(BUZZER, 500)
    pwmPin.start(50)
    rospy.sleep(data.data)
    pwmPin.stop()


def listener():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZER, GPIO.OUT)

    rospy.init_node('buzzer', anonymous=True)
    rospy.Subscriber("buzzerControl", Float32, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
    

