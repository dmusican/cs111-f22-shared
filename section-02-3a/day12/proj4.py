from images import *

win = ImageWin(480, 640, "Me!!!!!")
dave = FileImage('dave-selfie.gif')
dave.draw(win)

for i in range(dave.getNumPixels()):
    #print(dave.getPixel1D(i))

    threshold = 150
    pixel = dave.getPixel1D(i)
    if pixel.getRed() > threshold and \
       pixel.getGreen() > threshold and \
       pixel.getBlue() > threshold:

        #dave.setPixel1D(i, Pixel(0,0,0))
        # replace with one pixel left
        dave.setPixel1D(i, dave.getPixel1D(i-1))



input("Waiting....")
