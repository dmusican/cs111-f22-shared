# A ball that moves around the screen
from graphics import *
from time import *

windowWidth = 500
windowHeight = 600
win = GraphWin("Game!", windowWidth, windowHeight)
win.setBackground('white')

location = win.getMouse()
print(type(location))
x = location.getX()
y = location.getY()
raddddddius = 30  # dumb name to make a point

shiftx = 10
shifty = 20
for i in range(1000):
    circ = Circle(Point(x,y), raddddddius)
    circ.draw(win)
    sleep(0.1)
    circ.undraw()
    x = (x + shiftx) % windowWidth
    y = (y + shifty) % windowHeight


keyPressed = input('Type something: ')