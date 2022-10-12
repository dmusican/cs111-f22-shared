


from images import *

def removeBright(image):

    newPic = image.copy()
    for i in range(newPic.getNumPixels()):
        pixel = newPic.getPixel1D(i)
        threshold = 150
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:
           newPic.setPixel1D(i, newPic.getPixel1D(i-1))

    return newPic



def main():
    win1 = ImageWin(700, 500, "Original")
    orig = FileImage('dave-selfie.gif')
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(700, 500, "Fixed")
    noBright.draw(win2)

    input("Looking....")

main()
