from images import *


def blur(original, width):
    newPic = original.copy()
    for i in range(newPic.getNumPixels()):
        #average of the range of the pixels in the original
        newPixel = Pixel(average(original, i, width, 0),
                         average(original, i, width, 1),
                         average(original, i, width, 2))
        newPic.setPixel1D(i, newPixel)

    return newPic


def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(),
                    "Original")
    orig.draw(win1)

    updated = blur(orig, 2)
    win2 = ImageWin(updated.getWidth(), updated.getHeight(),
                    "Updated")
    updated.draw(win2)

    input("Look at me...")

if __name__=="__main__":
    main()
