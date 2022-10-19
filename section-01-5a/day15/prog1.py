
def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Original")
    orig.draw(win1)

    updated = blur(orig, 5)
    win2 = ImageWin(orig.getWidth(), orig.getHeight(), "Blurred")
    updated.draw(win2)

    input("Look at me!")

if __name__=="__main__":
    main()
