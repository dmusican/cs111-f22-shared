from images import *

def flip(image):
    newImage = image.copy()

    for i in range(image.getWidth()):
        for j in range(image.getHeight()):
            oppositePixel = image.getPixel2D(i, image.getHeight()- j - 1)
            newImage.setPixel2D(i, j, oppositePixel)
    return newImage


def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)

    flipped = flip(orig)
    win2 = ImageWin(flipped.getWidth(), flipped.getHeight(), "whoa")
    flipped.draw(win2)
    input("Look at me!")

if __name__=="__main__":
    main()
