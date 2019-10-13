class RealSound:
    def play(self, emotion):
        pass

class MockSound:
    def play(self, mood):
        if emotion in ['anger', 'disgust', 'fear']:
            print("Playing negative noise..")
        elif emotion == 'happy':
            print("Playing happy noise...")
        elif emotion == 'surprise':
            print("Playing surprised noise...")

def CheerbotSound(mock=True):
    if mock:
        return MockSound()
    else:
        return RealSound()

if __name__ == '__main__':
    # Using this to test the sound module
    sound = CheerbotSound(mock=False)
    sound.play('happy')
    sound.play('anger')
    sound.play('surprise')
