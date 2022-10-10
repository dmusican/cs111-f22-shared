from images import *
from time import sleep

win = ImageWin(500, 700, "Me!!!!!!")
dave = FileImage("dave-selfie.gif")
dave.draw(win)

for i in range(dave.getNumPixels()):
    pixel = dave.getPixel1D(i)
    threshold = 200
    if pixel.getRed() > threshold and \
       pixel.getGreen() > threshold and \
       pixel.getBlue() > threshold:
       dave.setPixel1D(i, Pixel(0,0,0))

input("Look at me...")
