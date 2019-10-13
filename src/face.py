#!/usr/bin/env python3
from PIL import Image
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

class RealFace:
    def show(self, emotion):
        #Raspberry pi config
        DC = 17
        RST = 23
        SPI_PORT = 0
        SPI_DEVICE = 0

        #Create TFT LCD display class
        disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

        #Initialize display
        disp.begin()

        image = Image.open("assets/ON.bmp")
        if emotion is "happy":
            image = Image.open("assets/OH.bmp")
        elif emotion is "sad":
            image = Image.open("assets/OS.bmp")

        #Resize the image and rotate to display
        image = image.rotate(90).resize((240, 320))

        #Draw the image on the display hardware
        disp.display(image)
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

if __name__ == '__main__':
    test = RealFace()
    test.show("happy")
