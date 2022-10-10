from images import *

win = ImageWin(500, 700, "Me!!!!!!")
dave = FileImage("dave-selfie.gif")
dave.draw(win)

for i in range(dave.getNumPixels()):
    pixel = dave.getPixel1D(i)

    if pixel.getRed() > 200 and pixel.getGreen() > 200 \
       and pixel.getBlue() > 200:
       dave.setPixel1D(i, Pixel(0,0,0))

input("Look at me...")
