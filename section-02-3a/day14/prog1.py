from images import *

def blur(original, width):
    newPic = original.copy()

    for i in range(newPic.getNumPixels()):


def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)
    input("Look at me!")

if __name__=="__main__":
    main()
