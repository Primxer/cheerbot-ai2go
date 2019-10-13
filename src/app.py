#!/usr/bin/env python3
from emotion import EmotionClassifier
from time import sleep

from face import CheerbotFace
from sound import CheerbotSound
from rover import CheerbotRover

if __name__ == '__main__':
    face = CheerbotFace(mock=False)
    sound = CheerbotSound(mock=True)
    rover = CheerbotRover(mock=False)

    with EmotionClassifier() as emoteClassifier:
        while True:
            succ, emotion = emoteClassifier.read()
            if succ:
                print("Found face: " + emotion)
                # Determine which face to display
                face.show(emotion)
                sound.play(emotion)
                rover.react(emotion)

                # Cooldown so it doesn't repeat
                sleep(1)
            else:
                print("Can't see face: " + emotion)
                rover.wander()
