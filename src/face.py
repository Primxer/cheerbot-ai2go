
class RealFace:
    def show(emotion):
        # Your code here
        pass

# For running code without needing an LCD display
class MockFace:
    def show(emotion):
        print("Displaying an emotion of " + emotion)


def CheerbotFace(mock=True):
    if mock:
        return MockFace()
    else:
        return RealFace()
