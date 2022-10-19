from images import *

def crop(image, xstart, xend, ystart, yend):
    newWidth = xend - xstart
    newHeight = yend - ystart
    newImage = EmptyImage(width, height):


def main():
    orig = FileImage("dave-selfie.gif")
    win1 = ImageWin(orig.getWidth(), orig.getHeight(),
                    "Image Processing")
    orig.draw(win1)

    # 30<->200 is x range (cols), 100<->250 is y range (rows)
    cropped = crop(orig, 30, 201, 100, 251)
    win2 = ImageWin(cropped.getWidth(), cropped.getHeight(),
                    "Cropped!")
    cropped.draw(win2)

if __name__=="__main__":
    main()
