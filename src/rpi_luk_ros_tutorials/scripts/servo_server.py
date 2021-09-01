#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
from time import sleep



def init():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11, GPIO.OUT)
  pwm = GPIO.PWM(11, 50)  
  pwm.start(7.5)
  return pwm

def left(pwm):
  pwm.ChangeDutyCycle(5)

def neutral(pwm):
  pwm.ChangeDutyCycle(7.5)

def right(pwm):
  pwm.ChangeDutyCycle(10)

def stop(pwm):
  pwm.stop()
  GPIO.cleanup()

def callback(data):
  pwm = init()
  rospy.loginfo(rospy.get_caller_id() + ' servo heard position %s', data.data)
  position = data.data 
  if position == 'left':
    left(pwm)
  elif position == 'right':
    right(pwm)
  elif position == 'neutral':
    neutral(pwm)
  else:
    rospy.loginfo("unknown position %s", position)
  sleep(2)
  stop(pwm)


def listener():
    rospy.init_node('servo_listener', anonymous=True)
    rospy.Subscriber('servo_position', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
