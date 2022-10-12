from images import *

def removeBright(brightImage):



def main():
    win1 = ImageWin(480, 640, "Original")
    orig = FileImage("dave-selfie.gif")
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(480, 640, "Fixed")
    noBright.draw(win2)

    input("Looking...")

main()
