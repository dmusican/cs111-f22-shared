from images import *

def removeBright(brightImage):
    newPic = brightImage.copy()
    for i in range(newPic.getNumPixels()):

        threshold = 150
        pixel = newPic.getPixel1D(i)
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:
            # replace with one pixel left
            newPic.setPixel1D(i,
                        newPic.getPixel1D(i-1))

    return newPic

def main():
    win1 = ImageWin(480, 640, "Original")
    orig = FileImage("dave-selfie.gif")
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(480, 640, "Fixed")
    noBright.draw(win2)

    input("Looking...")

main()
