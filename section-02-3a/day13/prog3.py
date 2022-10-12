from images import *

def removeBright(brightImage):
    for i in range(brightImage.getNumPixels()):

        threshold = 150
        pixel = brightImage.getPixel1D(i)
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:
            # replace with one pixel left
            brightImage.setPixel1D(i,
                        brightImage.getPixel1D(i-1))

    return brightImage

def main():
    win1 = ImageWin(480, 640, "Original")
    orig = FileImage("dave-selfie.gif")
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(480, 640, "Fixed")
    noBright.draw(win2)

    input("Looking...")

main()
