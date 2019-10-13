#!/usr/bin/env python3
from emotion import EmotionDetector
from face import CheerbotFace
from time import sleep

if __name__ == '__main__':
    face = CheerbotFace(mock=True)

    with EmotionClassifier() as face:
        while True:
            succ, emotion = face.read()
            if succ:
                # Determine which face to display
                to_display = emotion
                if emotion in ['happy', 'neutral']:
                    to_display = 'positive'
                elif emotion in ['disgust', 'fear', 'sad']:
                    to_display = 'negative'

                face.show(to_display)

                # Cooldown so it doesn't repeat
                sleep(1)
            else:
                print("Can't see a face just yet")
