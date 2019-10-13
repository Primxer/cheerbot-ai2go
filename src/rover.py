from time import sleep

#######Pin Asssignments for the Motor Controller
#RightMotorSpeed pin  5  //blue wire pi18
#RightMotorDir   pin  0  //purple wire pi12
#LeftMotorSpeed  pin  4  //gray wire pi13
#LeftMotorDir    pin  2  //white wire pi19


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
