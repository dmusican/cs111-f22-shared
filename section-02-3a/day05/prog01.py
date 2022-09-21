# Ball flying around a screen
from graphics import *
from time import *
windowWidth = 500
windowHeight = 600
win = GraphWin("Game!", windowWidth, windowHeight)
win.setBackground('white')

# Have user click in window to draw a ball
location = win.getMouse()
x = location.getX()
y = location.getY()
circ = Circle(Point(x,y), 20)
circ.draw(win)

# Move the ball in a loop
for i in range(100):
    circ = Circle(Point(x,y), 20)
    circ.draw(win)
    sleep(0.1)
    circ.undraw()
    x = x + 10
    y = y + 20

keyEntered = input("Enter something: ")
