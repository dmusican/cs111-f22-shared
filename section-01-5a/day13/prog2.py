

def removeBright(image):


    for i in range(dave.getNumPixels()):
        pixel = dave.getPixel1D(i)
        threshold = 150
        if pixel.getRed() > threshold and \
           pixel.getGreen() > threshold and \
           pixel.getBlue() > threshold:
           dave.setPixel1D(i, dave.getPixel1D(i-1))





def main():
    win1 = ImageWin(700, 500, "Original")
    orig = FileImage('dave-selfie.jpg')
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(700, 500, "Fixed")
    noBright.draw(win2)

    input("Looking....")

main()
