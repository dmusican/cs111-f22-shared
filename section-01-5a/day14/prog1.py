from images import *

def average(image, location, width, rgbChoice):
    total = 0
    for i in range(-width, width+1):
        pixel_i = image.getPixel1D(location + i)

        total = total + pixel_i[rgbChoice]

    mean = total // (2*width + 1)
    return mean


def blur(original, width):
    newPic = original.copy()
    for i in range(width, newPic.getNumPixels()-width):
        #average of the range of the pixels in the original
        newPixel = Pixel(average(original, i, width, 0),
                         average(original, i, width, 1),
                         average(original, i, width, 2))
        newPic.setPixel1D(i, newPixel)

    return newPic


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
