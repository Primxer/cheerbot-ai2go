from time import sleep
From RPi.GPIO import GPIO

#######Pin Asssignments for the Motor Controller
#RightMotorSpeed pin  5  //blue wire pi18
#RightMotorDir   pin  0  //purple wire pi12
#LeftMotorSpeed  pin  4  //gray wire pi13
#LeftMotorDir    pin  2  //white wire pi19

#######Pin Setup
GPIO.setmode(GPIO.BCM)
LOW = 0
HIGH = 0
rightDir = LOW
rightSpeed = LOW
leftDir = LOW
leftSpeed = LOW

GPIO.setup(rightDir,GPIO.OUT)
GPIO.setup(rightSpeed,GPIO.OUT)
GPIO.setup(leftDir,GPIO.OUT)
GPIO.setup(leftSpeed,GPIO.OUT)


# Skeleton for where the real rover code would be
class RealRover:
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
    rover = CheerbotRover(mock=True)
    rover.react('happy')
    rover.react('fear')

def forward()
    GPIO.output(rightDir,GPIO.HIGH)
    GPIO.output(leftDir,GPIO.HIGH)
    GPIO.output(rightSpeed,GPIO.HIGH)
    GPIO.output(leftSpeed,GPIO.HIGH)

def backward()
    GPIO.output(rightDir,GPIO.LOW)
    GPIO.output(leftDir,GPIO.LOW)
    GPIO.output(rightSpeed,GPIO.HIGH)
    GPIO.output(leftSpeed,GPIO.HIGH)

def right()
    GPIO.output(rightDir,GPIO.LOW)
    GPIO.output(leftDir,GPIO.HIGH)
    GPIO.output(rightSpeed,GPIO.HIGH)
    GPIO.output(leftSpeed,GPIO.HIGH)

def left()
    GPIO.output(rightDir,GPIO.HIGH)
    GPIO.output(leftDir,GPIO.LOW)
    GPIO.output(rightSpeed,GPIO.HIGH)
    GPIO.output(leftSpeed,GPIO.HIGH)

def stop()
    GPIO.output(rightDir,GPIO.LOW)
    GPIO.output(leftDir,GPIO.LOW)
    GPIO.output(rightSpeed,GPIO.LOW)
    GPIO.output(leftSpeed,GPIO.LOW)


#####We must make sure the motors are stopped at the end
stop()
