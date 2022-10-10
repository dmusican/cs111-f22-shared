from images import *

win = ImageWin(500, 700, "Me!!!!!!")
dave = FileImage("dave-selfie.gif")
dave.draw(win)

for i in range(dave.getNumPixels()):
    print(dave.getPixel1D(i))

input("Look at me...")
