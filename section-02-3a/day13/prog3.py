from images import *

def removeBright(brightImage):
    for i in range(brightImage.getNumPixels()):

        threshold = 150
        pixel = brightImage.getPixel1D(i)
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:

            #dave.setPixel1D(i, Pixel(0,0,0))
            # replace with one pixel left
            dave.setPixel1D(i, dave.getPixel1D(i-1))



def main():
    win1 = ImageWin(480, 640, "Original")
    orig = FileImage("dave-selfie.gif")
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(480, 640, "Fixed")
    noBright.draw(win2)

    input("Looking...")

main()
