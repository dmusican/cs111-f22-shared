from images import *

def blur(original, width):
    newPic = original.copy()

    for i in range(newPic.getNumPixels()):
        #average of pixels around pixel i
        newPixelValue = Pixel(average(original, i, width, 0),
                              average(original, i, width, 1),
                              average(original, i, width, 2))
        newPic.setPixel1D(i, newPixelValue)

    return newPic

def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)
    input("Look at me!")

    blurred = blur(orig, 5)

if __name__=="__main__":
    main()
