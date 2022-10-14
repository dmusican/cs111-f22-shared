from images import *

def main():
    orig = FileImage('dave-selfie.jpg')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Original")
    orig.draw(win1)
    input("Look at me...")

if __name__=="__main__":
    main()
