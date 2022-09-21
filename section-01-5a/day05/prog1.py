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
circ = Circle(Point(x,y), raddddddius)
circ.draw(win)

shiftx = 10
shifty = 20
for i in range(100):
    sleep(0.1)
    circ.move(shiftx, shifty)


keyPressed = input('Type something: ')