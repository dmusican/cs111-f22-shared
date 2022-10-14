from images import *

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
