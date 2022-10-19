from images import *

def flip(original):
    newPic = original.copy()






    return newPic

def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Original")
    orig.draw(win1)

    updated = flip(orig)
    win2 = ImageWin(orig.getWidth(), orig.getHeight(), "Flipped")
    updated.draw(win2)

    input("Look at me!")

if __name__=="__main__":
    main()
