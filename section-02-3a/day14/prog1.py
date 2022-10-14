from images import *

def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)

if __name__=="__main__":
    main()
