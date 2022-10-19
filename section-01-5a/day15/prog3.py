from images import *

def crop(original, xstart, xend, ystart, yend):
    newWidth = xend - xstart
    newHeight = yend - ystart




    return newPic

def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Original")
    orig.draw(win1)

    updated = crop(orig, 30, 201, 100, 251)
    win2 = ImageWin(orig.getWidth(), orig.getHeight(), "Cropped")
    updated.draw(win2)

    input("Look at me!")

if __name__=="__main__":
    main()
