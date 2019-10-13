#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO
import atexit

#######Pin Asssignments for the Motor Controller
#RightMotorSpeed pin  5  //blue wire pi pin 18
#RightMotorDir   pin  0  //purple wire pi pin 12
#LeftMotorSpeed  pin  4  //gray wire pi pin 13
#LeftMotorDir    pin  2  //white wire pi pin 19

#######Pin Setup
GPIO.setmode(GPIO.BCM)
LOW = 0
HIGH = 1
rightDir = 12
rightSpeed = 18
leftDir = 19
leftSpeed = 13

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

    def left(self):
        GPIO.output(rightDir, GPIO.LOW)
        GPIO.output(leftDir, GPIO.HIGH)
        GPIO.output(rightSpeed, GPIO.HIGH)
        GPIO.output(leftSpeed, GPIO.HIGH)

    def right(self):
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
        if emotion is "happy":
            self.right()
            sleep(1.0)
            self.stop()
            self.left()
            sleep(2.0)
            self.stop()
            self.right()
            sleep(1.0)
            self.stop()
        elif emotion is "sad":
            self.forward()
            sleep(0.25)
            self.stop()
            self.left()
            sleep(0.25)
            self.stop()
            self.right()
            sleep(0.5)
            self.stop()
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

# Clean up GPIO ports at program exit
def __cleanup__():
    GPIO.cleanup([rightDir, rightSpeed, leftDir, leftSpeed])
atexit.register(__cleanup__)


if __name__ == '__main__':
    rover = RealRover()
    rover.react("happy")
    sleep(2)
    rover.react("sad")
