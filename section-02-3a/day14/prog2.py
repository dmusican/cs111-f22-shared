from images import *


def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)

    flipped = flip(orig, 5)
    win2 = ImageWin(flipped.getWidth(), flipped.getHeight(), "whoa")
    flipped.draw(win2)
    input("Look at me!")

if __name__=="__main__":
    main()
