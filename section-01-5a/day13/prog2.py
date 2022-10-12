


from images import *

def removeBright(image):

    for i in range(image.getNumPixels()):
        pixel = image.getPixel1D(i)
        threshold = 150
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:
           image.setPixel1D(i, image.getPixel1D(i-1))

    return image



def main():
    win1 = ImageWin(700, 500, "Original")
    orig = FileImage('dave-selfie.jpg')
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(700, 500, "Fixed")
    noBright.draw(win2)

    input("Looking....")

main()
