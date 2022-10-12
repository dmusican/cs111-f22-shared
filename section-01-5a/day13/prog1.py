from images import *
from time import sleep

win = ImageWin(500, 700, "Me!!!!!!")
dave = FileImage("dave-selfie.gif")
dave.draw(win)

for i in range(dave.getNumPixels()):
    pixel = dave.getPixel1D(i)
    threshold = 150
    if pixel.getRed() > threshold and \
       pixel.getGreen() > threshold and \
       pixel.getBlue() > threshold:
       dave.setPixel1D(i, dave.getPixel1D(i-1))

input("Look at me...")
