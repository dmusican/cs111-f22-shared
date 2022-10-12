



def main():
    win1 = ImageWin(700, 500, "Original")
    orig = FileImage('dave-selfie.jpg')
    orig.draw(win1)

    noBright = removeBright(orig)
    win2 = ImageWin(700, 500, "Fixed")
    noBright.draw(win2)

    input("Looking....")

main()
