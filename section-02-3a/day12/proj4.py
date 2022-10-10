from images import *

win = ImageWin(480, 640, "Me!!!!!")
dave = FileImage('dave-selfie.gif')
dave.draw(win)

for i in range(dave.getNumPixels()):
    print(dave.getPixel1D(i))

    pixel = dave.getPixel1D(i)
    if pixel.getRed() > 200 and pixel.getGreen() > 200 \
       and pixel.getBlue() > 200:

        dave.setPixel1D(i, Pixel(0,0,0))



input("Waiting....")
