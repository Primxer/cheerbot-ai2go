#!/usr/bin/env python3
from emotion import EmotionClassifier
from time import sleep

from face import CheerbotFace
from sound import CheerbotSound
from rover import CheerbotRover

if __name__ == '__main__':
    face = CheerbotFace(mock=True)
    sound = CheerbotSound(mock=True)

    with EmotionClassifier() as face:
        while True:
            succ, emotion = face.read()
            if succ:
                # Determine which face to display
                face.show(emotion)
                sound.play(emotion)
                rover.react(emotion)


                # Cooldown so it doesn't repeat
                sleep(1)
            else:
                rover.wander()
