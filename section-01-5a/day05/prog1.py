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
radius = 30
circ = Circle(Point(x,y), radius)
circ.draw(win)

for i in range(100):
    shiftx = 10
    shifty = 20
    sleep(0.1)
    circ.move(shiftx, shifty)


keyPressed = input('Type something: ')