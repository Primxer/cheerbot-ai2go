#!/usr/bin/env python3
from tempdir import tempdir
from os import path
import xnornet

from pprint import pprint
from subprocess import Popen, DEVNULL

class EmotionClassifier:
    NO_READ = "Can't read webcam"
    NO_SAVE = "Can't save image"
    NO_FACE = "Can't find face to classify."

    # Listed on README.txt from the AI2GO library
    emotions = ['anger', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    imgpath = path.join(tempdir(), 'live.jpg')

    def __init__(self):
        self.model = xnornet.Model.load_built_in()

    def read(self):
        proc = Popen(["fswebcam", "--no-banner", EmotionClassifier.imgpath],
                     stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL, close_fds=True)
        proc.wait()

        if proc.returncode != 0:
            return False, EmotionClassifier.NO_READ

        capture_jpg = None
        with open(EmotionClassifier.imgpath, 'rb') as f:
            capture_jpg = f.read()

        xinput = xnornet.Input.jpeg_image(capture_jpg)
        objects = self.model.evaluate(xinput)
        if len(objects) == 0:
            return False, EmotionClassifier.NO_FACE

        return True, objects[0].label

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

if __name__ == '__main__':
    rover = RoverBot()
    with EmotionClassifier() as face:
        while True:
            succ, emotionOrErrMsg = face.read()
            if succ:
                print("Face detection: " + emotionOrErrMsg)
            else:
                print("Error: " + emotionOrErrMsg)
