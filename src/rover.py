#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO

#######Pin Asssignments for the Motor Controller
#RightMotorSpeed pin  5  //blue wire pi18
#RightMotorDir   pin  0  //purple wire pi12
#LeftMotorSpeed  pin  4  //gray wire pi13
#LeftMotorDir    pin  2  //white wire pi19

#######Pin Setup
GPIO.setmode(GPIO.BCM)
LOW = 0
HIGH = 0
rightDir = 0
rightSpeed = 5
leftDir = 2
leftSpeed = 4

GPIO.setup(rightDir, GPIO.OUT)
GPIO.setup(rightSpeed, GPIO.OUT)
GPIO.setup(leftDir, GPIO.OUT)
GPIO.setup(leftSpeed, GPIO.OUT)


# Skeleton for where the real rover code would be
class RealRover:
    def forward(self):
        GPIO.output(rightDir, GPIO.HIGH)
        GPIO.output(leftDir, GPIO.HIGH)
        GPIO.output(rightSpeed, GPIO.HIGH)
        GPIO.output(leftSpeed, GPIO.HIGH)

    def backward(self):
        GPIO.output(rightDir, GPIO.LOW)
        GPIO.output(leftDir, GPIO.LOW)
        GPIO.output(rightSpeed, GPIO.HIGH)
        GPIO.output(leftSpeed, GPIO.HIGH)

    def right(self):
        GPIO.output(rightDir, GPIO.LOW)
        GPIO.output(leftDir, GPIO.HIGH)
        GPIO.output(rightSpeed, GPIO.HIGH)
        GPIO.output(leftSpeed, GPIO.HIGH)

    def left(self):
        GPIO.output(rightDir, GPIO.HIGH)
        GPIO.output(leftDir, GPIO.LOW)
        GPIO.output(rightSpeed, GPIO.HIGH)
        GPIO.output(leftSpeed, GPIO.HIGH)

    def stop(self):
        GPIO.output(rightDir, GPIO.LOW)
        GPIO.output(leftDir, GPIO.LOW)
        GPIO.output(rightSpeed, GPIO.LOW)
        GPIO.output(leftSpeed, GPIO.LOW)

    def react(self, emotion):
        pass

    def wander(self):
        pass


# Mock code to describe how the rover should behave
class MockRover:
    def react(self, emotion):
        if emotion == 'happy':
            print("Doing a circle!")
        elif emotion == 'fear':
            print("shulking away...")

    def wander(self):
        print("Wandering....")
        sleep(1)


def CheerbotRover(mock=True):
    if mock:
        return MockRover()
    else:
        return RealRover()


if __name__ == '__main__':
    rover = RealRover()
    rover.forward()