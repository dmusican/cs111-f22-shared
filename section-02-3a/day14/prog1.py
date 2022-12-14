from images import *

def average(image, center, width, rgbChoice):
    total = 0
    for i in range(-width, width+1):
        pixel_i = image.getPixel1D(center + i)
        total = total + pixel_i[rgbChoice]
    mean = total // (2*width + 1)
    return mean

def blur(original, width):
    newPic = original.copy()

    for i in range(width, newPic.getNumPixels()-width):
        #average of pixels around pixel i
        newPixelValue = Pixel(average(original, i, width, 0),
                              average(original, i, width, 1),
                              average(original, i, width, 2))
        newPic.setPixel1D(i, newPixelValue)

    return newPic

def main():
    orig = FileImage('dave-selfie.gif')
    win1 = ImageWin(orig.getWidth(), orig.getHeight(), "Dave")
    orig.draw(win1)

    blurred = blur(orig, 5)
    win2 = ImageWin(blurred.getWidth(), blurred.getHeight(), "whoa")
    blurred.draw(win2)
    input("Look at me!")

if __name__=="__main__":
    main()
